# Signed Decisions (SigDec)

A small folder of ranked, signed design rules that AI agents and people read
from one source.

AI agents now build screens from design systems, and they follow every rule
they are given. Those rules usually live in a hand-written agent file
(`AGENTS.md`, `CLAUDE.md` and similar). That file has three faults:

- **Length.** It grows one line at a time. Rules in the middle of a long file
  are the ones a model retrieves worst.
- **Silence.** When an agent ignores a rule, nothing reports it.
- **Secrecy.** It sits in a repository and is edited by a few people. The
  product managers, designers and lawyers who make the decisions never see
  what the machine is told about them.

Signed Decisions keeps the rules that cross components in one folder, and
generates everything a machine reads from that folder.

**Start here:** open `playground/index.html` in a browser for the whole
model with interactive diagrams, then look through `examples/harbor/`.

## What a signed decision is

One short file. It holds a rule that more than one component or flow must
follow, and four things nothing else carries:

| Field | What it answers |
| --- | --- |
| **Scope** | Which components, flows or actions does this bind? |
| **Rank** | How binding is it? `MUST`, `SHOULD` or `MAY` |
| **Signer** | Which function owns it, and who do I ask why? |
| **Review date** | When does someone have to look at it again? |

```yaml
---
id: DEC-0004
status: accepted
rank: MUST
scope: [action:delete, action:transfer, state:destructive]
decision-makers: [product, legal]
date: 2026-09-14
review: 2027-09
justification: history/destructive-actions.md
verify: confirm-before-destructive
---
Any action that removes data or moves money MUST confirm first.
Because in shared accounts the harm falls on the person who did not act.
Not: immediate action with an undo message.
Do: a dialog that names the consequence.
```

The example comes from Harbor, a fictional bank used throughout this
repository.

## What it is not

Signed Decisions is deliberately narrow. Most rules belong somewhere else.

| This kind of statement | Lives in |
| --- | --- |
| A value: a colour, a size, a duration | A design token |
| A rule about one component | That component's CRD (see Credits) |
| The reasoning, the options ruled out | The decision history, linked from the decision |
| A working rule for agents ("ask before writing") | The hand-written part of the agent file |
| A fact about the current files (counts, names) | Nowhere. Read it live |
| **A rule several components or flows must follow** | **A signed decision** |

Two tests before writing one: could someone plausibly propose the opposite?
(That bar comes from Cassie Groos's CRD.) And is it free of values? If either
answer is no, it is not a decision.

## How it works

```
people decide ──▶ decisions/ ──▶ index.json ──▶ agents, by scope
                      │       ├─▶ agent file block (generated)
                      │       ├─▶ a page anyone can open
                      │       └─▶ one check per decision ──▶ signer
                      └── links to the history for the reason
```

1. **Capture.** Someone types a rough sentence where the decision is made.
   An assistant formats it and asks one question to set the rank: if this
   ships wrong, is it unlawful or unsafe, or only inconsistent?
2. **Sign.** The function that owns the rule approves the change. Approval
   is the signature. Repository review rules (`CODEOWNERS`) can enforce it.
3. **Compile.** The folder is validated and compiled into an index. The
   agent file gets a short generated block marked "do not edit".
4. **Deliver.** Before building, an agent asks for the decisions that match
   the components and actions in its plan. It receives a handful, strictest
   first, each with its ID.
5. **Check.** Each decision names a check. Checks run when the design files
   or the code change, and a failure goes to the signer.
6. **Review.** On its review date, or earlier if its check fails or a call
   is logged against it, a decision is renewed, reworded, retired or
   promoted.
7. **Promote.** A decision that has proved stable becomes a token, a
   statement in a CRD, or a lint rule, and leaves the folder.

### When two decisions disagree

1. The stricter rank wins.
2. Same rank: the one that names the other in `overrides` wins.
3. Then the narrower scope.
4. Then ask the person who wrote the brief.

Two `MUST`s that conflict are never resolved by the agent. It stops and
names both signers.

### When a decision is unclear in use

The agent reads the justification. If that does not settle it, it asks the
designer who launched it to make the call, with one line on why, and
finishes the work. Afterwards it logs the conflict and the call, marks the
work, and flags the entry to the decision's signers. The call applies to
that piece of work only, until the signers confirm, reword or overrule it.

### The agent file

The agent file has two parts. People write the working context: where
things are, which tools to run. The decisions block is generated:

```markdown
<!-- BEGIN GENERATED: decisions — do not edit; run sigdec.py compile -->
Before building or changing a component, look up its decisions:
decisions/index.json, filtered by component, flow or action
(or run `sigdec.py scope <keys>`).

Always apply:
- DEC-0004 · MUST — Any action that removes data or moves money MUST confirm first.
- DEC-0042 · MUST — An icon-only button MUST have an accessible name.
<!-- END GENERATED -->
```

Only decisions that apply to every task appear in the block. The rest are
fetched by scope.

## Repository layout

```
examples/harbor/        a sample project: decisions, history, component
                        records, checks, tokens, a brief and an agent file
playground/index.html   the working model as an interactive page
experiment/             Experiment 1: the Figma file with the method, the results
                        and every run
.claude/skills/sig-dec/ a Claude skill and the tool it uses (sigdec.py)
REFERENCES.md           credits and sources
```

## The tool and the skill

`sigdec.py` validates the records, compiles the index and the agent file
block, looks decisions up by scope and lists what is waiting for review.
Python 3, no dependencies.

```
S=.claude/skills/sig-dec/scripts/sigdec.py
python3 $S --root examples/harbor validate
python3 $S --root examples/harbor compile
python3 $S --root examples/harbor scope component:data-table action:delete
python3 $S --root examples/harbor review
```

The skill in `.claude/skills/sig-dec/` teaches a Claude agent to use the
folder: look decisions up before building, check a product brief, check a
CRD, test a linked Figma file against each decision's check,
audit an agent file, draft a decision, log a designer's call and run the
review queue. Copy the folder into your own project's `.claude/skills/`.

The checks in `examples/harbor/checks/` are written instructions that an
agent follows against a design file. They are not automated tests, and the
skill has not yet been tried on a real project.

## Evidence

One controlled experiment, concluded 5 October 2026. One agent built the
same three-screen flow under six briefings, five runs each, with
predictions written down before the first run.

**What held**

- Given the same nine rules, agents with ranked, scoped decisions built the
  safe path where two rules collided in **9 runs of 10** (10 of 10 counting
  one hidden dialog). Every other briefing managed **0 of 20**.
- The standard rules file named the conflict in its own report in 5 runs of
  5, then built the unsafe option in 5 of 5.
- No out-of-scope decision was applied in any run.

**What did not hold**

- It did not use fewer tokens.
- It did not make runs steadier.
- The test of an unforeseen case was spoiled: the brief leaked the answer.
- The reason and the rank were delivered together, so their effects cannot
  be separated yet.
- No human rated any output. Quality scores came from a model acting as
  judge and are labelled as such.

Under the pre-registered rule the verdict was **adjust**, not go. Limits:
one model, one flow, five runs per condition.

The record is in `experiment/`: the protocol fixed before the first run
(`PROTOCOL.md`), the report (`REPORT.md`) and a Figma file with every screen
the agents built. The runner, the scoring files and the product brief are
not published yet, so the experiment cannot be rerun from this repository.

## Status

| Part | Status |
| --- | --- |
| A rank and a scope on each decision | Tested in Experiment 1, in an earlier format (see below) |
| Delivery by scope | Tested in Experiment 1 |
| The record format shown here (MUST, SHOULD, MAY) | Revised after the experiment; not yet tested |
| Validation, index, generated agent file block | Built (`sigdec.py`) |
| Checks against a design file | Designed; run by hand once |
| Capture, signing, call logs | Designed |
| Review and promotion | Designed |

**The format changed after the experiment.** The decisions the agents
received used the strictness words *working*, *binding* and *mandatory*, in
a longer record with the signer's name. The principle tested, a rank plus a
scope, is the same. The MUST, SHOULD and MAY wording and the fields in this
repository came afterwards, and Run 2 will test them.

Nothing yet shows that people will write and sign decisions. Decision
records have failed this way before: in one study of projects that adopted
them, about half wrote fewer than five.

## Trying it

Start small, and stop if it does not take.

1. **An afternoon.** Open the file your agents read. For each design rule,
   ask: is this written anywhere a designer would see it, and is it still
   true?
2. **A day.** Write the rules that fail as ranked sentences, one file each.
   Ask the owning function to sign, reword or reject each one.
3. **A week.** Generate the agent file block from the folder.
4. **Six weeks.** If nobody has added or changed a decision, stop. Do not
   rescue it with more process.

## Credits

Signed Decisions is a concept by Phillip Sanders, developed at Thiga.

It is built to support the **CRD (Component Requirements Document) by
Cassie Groos**: one co-authored file per component that holds its
requirements, what was ruled out and the decisions behind it. See her
article "Probabilistic isn't a dirty word…" (27 August 2026). A CRD holds
what is true of one component; Signed Decisions holds only the rules that
cross components, which a CRD can cite.

It borrows from the Y-statement, architecture decision records, RFC 2119
requirement levels and recent studies of how models use instructions. Full
references and thanks are in `REFERENCES.md`.

## Licence

Code is MIT (`LICENSE`). Documentation, the playground and the experiment
report are CC BY 4.0 (`LICENSE-docs`).
