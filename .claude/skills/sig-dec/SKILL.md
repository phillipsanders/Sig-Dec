---
name: sig-dec
description: Work with a Signed Decisions folder (decisions/DEC-*.md). Use when asked to look up which decisions apply to a component, flow or action; check a product brief or PRD against the decisions; check a CRD (CRD) against them; test a linked Figma file against the decisions' checks; audit an agent file (AGENTS.md, CLAUDE.md) for unsigned design rules; propose, reword or retire a decision; log a designer's call when a decision is unclear; show the review queue; or compile the index and the agent file block. Also use before building or changing any component in a project that has a decisions/ folder.
---

# Signed Decisions

A signed decision is one short file holding a rule that more than one component or flow must follow, with
a rank (MUST, SHOULD, MAY), a scope, the functions that signed it and a review date. Everything a machine
reads is generated from the `decisions/` folder.

Find the project root first: the folder that contains `decisions/`. Pass it as `--root` if it is not the
working directory. The tool is `scripts/sigdec.py` in this skill's folder (Python 3, no dependencies).

```
python3 <skill>/scripts/sigdec.py --root <project> validate
python3 <skill>/scripts/sigdec.py --root <project> compile
python3 <skill>/scripts/sigdec.py --root <project> scope <key> [<key>...]
python3 <skill>/scripts/sigdec.py --root <project> review
```

## Rules that apply to every task

- **You never sign.** You draft, check and report. A decision is live only when the function that owns it
  approves the change. Never set `status: accepted` yourself, and never change a rank or a scope without
  being asked.
- **Never edit generated files** (`decisions/index.json`, the block between `BEGIN GENERATED` and
  `END GENERATED`). Change the records and run `compile`.
- **Design files are read-only.** Read Figma through whatever Figma tool the session has. Write to Figma
  only when the user asks, and only what they name.
- **Do not resolve two MUSTs.** If two MUST decisions conflict, stop and name both sets of signers.
- **Name functions, not people**, in decisions, logs and reports.
- **Say what you could not check.** A check you did not run is reported as not run, never as passed.

## 1. Look up decisions before building

1. List what the task touches as scope keys from `decisions/scopes.txt`: `component:`, `flow:`, `action:`,
   `content:`, `state:`.
2. Run `scope` with those keys. Apply what comes back, strictest first, and cite each ID you applied in
   your report.
3. If two returned decisions disagree: the stricter rank wins; at the same rank, the one that names the
   other in `overrides`; then the narrower scope; then ask the person who wrote the brief.
4. If no decision applies, say so. Do not invent one.

## 2. When a decision is unclear in use

1. Read its justification (the `justification:` path in the record).
2. If that does not settle it, ask the person who launched you to make the call, in one question, with the
   two options and a request for one line on why. Do not guess, and do not wait for the signers.
3. Finish the work with their answer.
4. After the work is complete:
   - write a call log in `decisions/calls/<date>-<slug>.md` (format below);
   - if the work is in Figma and the user agrees, add an annotation on the frame that names the decision
     and the call;
   - tell the user who the log is flagged to (the decision's `decision-makers`), and offer to draft the
     comment or message that tags them.
5. Say plainly that the call applies to this piece of work only, until the signers confirm, reword or
   overrule it.

```markdown
---
decision: DEC-0004
date: 2026-11-15
work: <what was built, and where>
flagged-to: [product, legal]
status: awaiting review
---
Conflict: <what the decision says, and what it does not settle>

Call (designer): <the choice>
Why: <their one line>

Applied to this work only, until the signers confirm, reword or overrule it.
```

## 3. Check a brief or PRD

Use when a product brief is written or changed, before design starts.

1. Read the brief. Split it into requirements.
2. For each requirement, work out its scope keys and run `scope`.
3. Sort every requirement into one of five results:

| Result | Meaning | What you write |
| --- | --- | --- |
| **Pinned** | A decision applies and the brief agrees | The ID, to carry into design |
| **Question** | The brief contradicts a SHOULD or MAY | One question for the author, naming the ID |
| **Stop** | The brief contradicts a MUST, or two records disagree | Who must decide, by function |
| **Gap** | Nothing covers it and it looks like law, money, safety or accessibility | Which function to ask |
| **CRD** | A single-component rule | The CRD statement to cite |

4. Report as a table, one row per requirement, then a one-line count. Do not rewrite the brief.

Try it on `examples/harbor/briefs/close-savings-account.md`.

## 4. Check a CRD

Use when a CRD is written or changed.

1. Read the record. For each numbered statement, find the decisions in its scope.
2. Mark each statement: **cite** (it restates a decision: keep it and add the ID), **close** (an `[open]`
   statement a decision already settles), **contradiction**, or **consistent**.
3. Check the record's `decisions:` list matches the IDs cited in its statements.
4. Report the contradictions first. A contradiction is corrected in the record, or raised with the
   decision's signers. Never change the decision to fit the record.

## 5. Test a Figma file against the decisions

Use when the design file is published, or when asked whether a file follows the decisions.

1. Ask for the Figma file or frame if none is linked. Confirm you will read only.
2. Run `validate`, then list every accepted or promoted decision that has a `verify:` field.
3. For each one:
   - `verify: <name>` → open `checks/<name>.md` and follow its steps against the file;
   - `verify: axe:<rule>` or `lint:<rule>` → this is a code check. Report it as "runs in code, not run
     here" unless you can run that tool.
4. Limit the test to the frames or components the user named. Say what you left out.
5. Report one row per decision: ID, rank, pass / fail / not run, the evidence (frame and layer names,
   counts), and the functions to send a failure to.
6. A failure is a finding, not a fix. Do not change the file. Offer to draft the message to the signers.

A check file states what to read and what counts as a pass. If a decision has no check, propose one in
`checks/` in the same shape as the existing ones.

## 6. Audit an agent file

Use to start a project, and every month or two after.

1. Read `AGENTS.md`, `CLAUDE.md` and any other instruction file agents load.
2. List every design rule outside the generated block. For each: is it recorded in a decision, a component
   record or the history? Is it still true in the design file or the code?
3. Sort each line: **stays** (working context), **becomes a decision** (draft it as `proposed`),
   **CRD** (name the CRD), **delete, read live** (counts, names, status), **not delivered**
   (a proposal nobody signed).
4. Report the split and the contradictions found. Change the agent file only if asked.

## 7. Propose, reword or retire a decision

1. Check it belongs here: it binds more than one component or flow; someone could plausibly propose the
   opposite; it contains no value. If not, say where it belongs (token, CRD, history, agent file).
2. Search the folder for a decision that already covers the scope. Prefer amending it.
3. Ask one question to set the rank: "If this ships wrong, is it unlawful, unsafe or inaccessible, or does
   the product only become inconsistent?" The first is MUST, the second SHOULD. A temporary working
   arrangement is MAY.
4. Write `decisions/DEC-<next number>.md` with `status: proposed`. First line: one sentence containing the
   rank word in capitals. Then `Because`, and where useful `Not:` and `Do:`.
5. Link the justification in `history/`, or set `justification: pending`. Write a new history entry as a
   Y-statement: "In the context of …, facing …, we decided …, and neglected …, to achieve …, accepting …".
6. Name a check in `verify:` if one can be written.
7. Run `validate`. Tell the user which functions must approve. Retiring or promoting sets `status:` and,
   for a promotion, `promoted-to:`.

## 8. Review queue and promotion

Run `review`. It lists decisions that were never signed, are past their review date, owe a justification,
or have a logged call. For each, propose one outcome with the evidence: **renew**, **reword**, **retire**
or **promote**.

A decision is ready to promote when its check has passed at every publish for a quarter and no call or
exception has been logged against it. Promotion moves the rule into a token description, a cited statement
in each affected CRD, or a lint rule, and sets `status: promoted`.

## 9. Compile

Run `compile` after any accepted change. It validates every record, writes `decisions/index.json` and
refreshes the generated block in the agent file. If validation fails, fix the record; do not edit the
output.
