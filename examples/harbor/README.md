# Harbor: a sample project

Harbor is a fictional bank. This folder shows what a project looks like once it uses Signed Decisions.
Everything here was written for this sample. Decisions DEC-0004 and DEC-0012 follow the two rules that
collided in Experiment 1; the other records, the signers and the dates are illustrative.

```
AGENTS.md              working context, plus a generated decisions block
CODEOWNERS             who must approve a change to a decision
decisions/             one file per signed decision
  README.md              how to write one, rank, conflict order
  scopes.txt             the scope keys a decision may use
  index.json             generated: what agents and tools read
  calls/                 calls made by designers when a decision was unclear
  rejected/              drafts that were declined, with the reason
history/               the full reasoning each decision links to
crd/              CRDs, which cite decision IDs
checks/                one check per decision, run against Figma or code
tokens/                design tokens; a promoted decision ends up here
briefs/                a product brief to try the brief check on
```

Try it from the repository root:

```
python3 .claude/skills/sig-dec/scripts/sigdec.py --root examples/harbor validate
python3 .claude/skills/sig-dec/scripts/sigdec.py --root examples/harbor compile
python3 .claude/skills/sig-dec/scripts/sigdec.py --root examples/harbor scope component:data-table action:delete
python3 .claude/skills/sig-dec/scripts/sigdec.py --root examples/harbor review
```
