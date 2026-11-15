#!/usr/bin/env python3
"""Signed Decisions: validate, compile, look up and review a decisions folder.

Standard library only. Usage (from the project root, or with --root):

    sigdec.py validate            check every record
    sigdec.py compile             validate, write decisions/index.json, refresh the agent file block
    sigdec.py scope KEY [KEY...]  decisions that apply to these scope keys, strictest first
    sigdec.py review              what is waiting for the signers

A project root holds decisions/DEC-*.md and, optionally, decisions/scopes.txt,
decisions/calls/, checks/ and AGENTS.md (or CLAUDE.md).
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

RANKS = ["MUST", "SHOULD", "MAY"]
STATUSES = ["proposed", "accepted", "promoted", "retired", "rejected"]
REQUIRED = ["id", "status", "rank", "scope", "decision-makers", "review"]
BEGIN = "<!-- BEGIN GENERATED: decisions — do not edit; run sigdec.py compile -->"
END = "<!-- END GENERATED -->"


def parse_value(raw):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        return [v.strip().strip("\"'") for v in inner.split(",") if v.strip()] if inner else []
    if raw in ("true", "false"):
        return raw == "true"
    return raw.strip("\"'")


def parse_record(path):
    """Front matter is a small YAML subset: `key: value`, inline lists, continuation lines."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("no front matter")
    meta, key = {}, None
    for line in m.group(1).splitlines():
        line = line.split(" #")[0].rstrip()
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z][\w-]*:", line):
            key, raw = line.split(":", 1)
            meta[key.strip()] = raw.strip()
            key = key.strip()
        elif key:
            meta[key] += " " + line.strip()
    meta = {k: parse_value(v) for k, v in meta.items()}
    return meta, m.group(2).strip()


def load(root):
    records, errors = [], []
    for path in sorted((root / "decisions").glob("DEC-*.md")):
        try:
            meta, body = parse_record(path)
            records.append({"meta": meta, "body": body, "path": path})
        except ValueError as e:
            errors.append(f"{path.name}: {e}")
    return records, errors


def scope_vocabulary(root):
    f = root / "decisions" / "scopes.txt"
    if not f.exists():
        return None
    return {l.strip() for l in f.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")}


def validate(root):
    records, errors = load(root)
    vocab = scope_vocabulary(root)
    ids = {r["meta"].get("id") for r in records}
    for r in records:
        m, name = r["meta"], r["path"].name
        err = lambda msg: errors.append(f"{name}: {msg}")
        for k in REQUIRED:
            if k not in m or m[k] in ("", []):
                err(f"missing {k}")
        if m.get("id") and m["id"] + ".md" != name:
            err("id does not match the file name")
        if m.get("rank") not in RANKS:
            err(f"rank must be one of {', '.join(RANKS)}")
        if m.get("status") not in STATUSES:
            err(f"status must be one of {', '.join(STATUSES)}")
        if not re.match(r"^\d{4}-\d{2}$", str(m.get("review", ""))):
            err("review must be YYYY-MM")
        for key in m.get("scope", []) if isinstance(m.get("scope"), list) else []:
            if not re.match(r"^[a-z]+:[a-z0-9*-]+$", key):
                err(f"scope key '{key}' is not kind:name")
            elif vocab is not None and not key.endswith(":*") and key not in vocab:
                err(f"scope key '{key}' is not in decisions/scopes.txt")
        for o in m.get("overrides", []) if isinstance(m.get("overrides"), list) else [m.get("overrides")]:
            if o and o not in ids:
                err(f"overrides {o}, which does not exist")
        j = m.get("justification", "")
        if j and j != "pending" and not (root / j.split("#")[0]).exists():
            err(f"justification file not found: {j}")
        v = m.get("verify", "")
        if v and ":" not in v and not (root / "checks" / f"{v}.md").exists():
            err(f"check not found: checks/{v}.md")
        if m.get("status") == "promoted" and not m.get("promoted-to"):
            err("promoted without promoted-to")
        found = [k for k in RANKS if re.search(rf"\b{k}\b", r["body"].split("\n")[0])]
        if m.get("rank") in RANKS and found != [m["rank"]]:
            err(f"the first line must contain {m['rank']} and no other rank keyword")
    return records, errors


def statement(body):
    lines = [l for l in body.splitlines() if l.strip()]
    out = {"say": lines[0] if lines else ""}
    for l in lines[1:]:
        for tag in ("Because", "Not", "Do"):
            if l.startswith(tag):
                out[tag.lower()] = l[len(tag):].lstrip(": ").strip()
    return out


def live(records):
    return [r for r in records if r["meta"].get("status") == "accepted"]


def index_entry(r):
    m = r["meta"]
    e = {"id": m["id"], "rank": m["rank"], "scope": m["scope"]}
    e.update(statement(r["body"]))
    for k in ("reader", "overrides", "verify"):
        if m.get(k):
            e[k] = m[k]
    return e


def order(records):
    return sorted(records, key=lambda r: (RANKS.index(r["meta"]["rank"]), r["meta"]["id"]))


def compile_(root):
    records, errors = validate(root)
    if errors:
        return errors
    entries = [index_entry(r) for r in order(live(records))]
    (root / "decisions" / "index.json").write_text(
        json.dumps({"decisions": entries}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    always = [r for r in order(live(records)) if r["meta"].get("always") is True]
    block = [BEGIN,
             "Before building or changing a component, look up its decisions:",
             "decisions/index.json, filtered by component, flow or action",
             "(or run `sigdec.py scope <keys>`).", ""]
    if always:
        block.append("Always apply:")
        block += [f"- {r['meta']['id']} · {r['meta']['rank']} — {statement(r['body'])['say']}" for r in always]
    block.append(END)
    for name in ("AGENTS.md", "CLAUDE.md"):
        f = root / name
        if f.exists() and BEGIN in f.read_text(encoding="utf-8"):
            text = f.read_text(encoding="utf-8")
            text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: "\n".join(block), text, flags=re.S)
            f.write_text(text, encoding="utf-8")
            print(f"updated {name}")
    print(f"wrote decisions/index.json ({len(entries)} live decisions)")
    return []


def matches(decision_key, query_key):
    if decision_key == query_key:
        return True
    kind = decision_key.split(":")[0]
    return decision_key.endswith(":*") and query_key.startswith(kind + ":")


def scope(root, keys):
    records, errors = validate(root)
    if errors:
        return errors
    hits = [r for r in live(records) if any(matches(d, q) for d in r["meta"]["scope"] for q in keys)]
    hit_ids = {r["meta"]["id"] for r in hits}
    overridden = {}
    for r in hits:
        o = r["meta"].get("overrides", [])
        for target in ([o] if isinstance(o, str) else o):
            if target in hit_ids:
                overridden[target] = r["meta"]["id"]
    if not hits:
        print("No live decision applies to: " + ", ".join(keys))
        return []
    for r in order(hits):
        m, s = r["meta"], statement(r["body"])
        note = f"   (set aside here: overridden by {overridden[m['id']]})" if m["id"] in overridden else ""
        print(f"{m['id']} · {m['rank']} — {s['say']}{note}")
        for k in ("not", "do"):
            if k in s:
                print(f"    {k.capitalize()}: {s[k]}")
    ranks = {r["meta"]["rank"] for r in hits if r["meta"]["id"] not in overridden}
    if len(hits) > 1:
        print("\nIf two of these disagree: the stricter rank wins; at the same rank, the one that")
        print("names the other in `overrides`, then the narrower scope, then ask the author.")
        if ranks == {"MUST"} and len(hits) - len(overridden) > 1:
            print("Two MUSTs that conflict are never resolved by an agent: stop and name both signers.")
    return []


def review(root, today):
    records, errors = validate(root)
    for e in errors:
        print("invalid   " + e)
    ym = today.strftime("%Y-%m")
    rows = []
    for r in records:
        m = r["meta"]
        who = ", ".join(m.get("decision-makers", []))
        if m.get("status") == "proposed":
            rows.append((m["id"], "never signed", who))
        if m.get("status") == "accepted":
            if str(m.get("review", "9999-99")) <= ym:
                rows.append((m["id"], f"review date reached ({m['review']})", who))
            if m.get("justification") == "pending":
                rows.append((m["id"], "owes a justification", who))
    calls = root / "decisions" / "calls"
    if calls.exists():
        for f in sorted(calls.glob("*.md")):
            try:
                m, _ = parse_record(f)
            except ValueError:
                continue
            if m.get("status") == "awaiting review":
                rows.append((m.get("decision", "?"), f"a call was logged ({f.name})", ", ".join(m.get("flagged-to", []))))
    if not rows:
        print("Nothing is waiting for review.")
    for r in rows:
        print(f"{r[0]:<10} {r[1]:<48} → {r[2]}")
    return []


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".", help="project root that holds decisions/")
    p.add_argument("--today", help="YYYY-MM-DD, for review (default: today)")
    p.add_argument("command", choices=["validate", "compile", "scope", "review"])
    p.add_argument("keys", nargs="*")
    a = p.parse_args()
    root = Path(a.root)
    if not (root / "decisions").is_dir():
        sys.exit(f"No decisions/ folder in {root.resolve()}")
    if a.command == "validate":
        records, errors = validate(root)
        if not errors:
            print(f"{len(records)} records valid")
    elif a.command == "compile":
        errors = compile_(root)
    elif a.command == "scope":
        if not a.keys:
            sys.exit("Give at least one scope key, for example: component:data-table action:delete")
        errors = scope(root, a.keys)
    else:
        today = datetime.date.fromisoformat(a.today) if a.today else datetime.date.today()
        errors = review(root, today)
    for e in errors:
        print("error: " + e, file=sys.stderr)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
