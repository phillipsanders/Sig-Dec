# Sig-Dec
 Signed Decisions: a small folder of ranked, signed design rules that cross components. Component records cite it, the AI agent file is generated from it, and a check compares it with the design files on every publish.
eople will read and quote: the concept documents, the experiment report and the README prose. It lets anyone reuse and adapt them as long as they credit you. MIT is written for software and says nothing clear about attribution for text.

How to set it up:
- Put LICENSE (MIT) at the root, so GitHub detects and displays it.
- Add LICENSE-docs (CC BY 4.0) and one line in the README: "Code is MIT. Documentation and the experiment report are CC BY 4.0."

When to choose differently:
- Apache 2.0 instead of MIT if you expect companies to adopt the tooling and want an explicit patent grant. It's longer and rarely needed for a project this size.
- CC BY-SA if you want adaptations of the concept to stay open under the same terms. It discourages some commercial reuse.
- No licence means nobody may legally reuse anything, which defeats the point of publishing.

Check first: the experiment was run on Thiga's time and resources. Under most employment contracts the employer owns that work, so Thiga may need to agree to the licence, and the copyright line may need to read "© 2026 Thiga" or name you both. Settle that before you publish.

✻ Baked for 10s · done 8:28 PM

❯ Provide a readme for this repo

The README below uses only the fictional bank example and contains no client material. It doesn't claim that any script exists: the repo layout section is a suggestion, and unbuilt parts are marked as planned.

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

## What a signed decision is

One short file. It holds a rule that more than one component or flow must
follow, and four things nothing else carries:

| Field | What it answers |
| --- | --- |
| **Scope** | Which components, flows or actions does t
| **Rank** | How binding is it? `MUST`, `SHOULD` or `MAY` |
| **Signer** | Which function owns it, and who do I ask
| **Review date** | When does someone have to look at it again? |

```yaml
---
id: DEC-0004
status: accepted
rank: MUST
scope: [action:delete, action:transfer]
decision-makers: [product, legal]
date: 2026-09-14
review: 2027-09
justification: history/destructive-actions.md
verify: confirm-before-destructive
---
Any action that removes data or moves money MUST confirm first.
Because in shared accounts the harm falls on the person
Not: immediate action with an undo message.
Do: a dialog that names the consequence.
```

The example comes from Harbor, a fictional bank used throughout this repo.

## What it is not

Signed Decisions is deliberately narrow. Most rules belong somewhere else.

| This kind of statement | Lives in |
| --- | --- |
| A value: a colour, a size, a duration | A design token |
| A rule about one component | That component's record
| The reasoning, the options ruled out | The decision history, linked from the decision |
| A working rule for agents ("ask before writing") | Th agent file |
| A fact about the current files (counts, names) | Nowhere. Read it live |
| **A rule several components or flows must follow** |

Two tests before writing one: could someone plausibly p
And is it free of values? If either answer is no, it is not a decision.

## How it works

```
people decide ──▶ decisions/ ──▶ index.json ──▶ agents,
                      │       ├─▶ agent file block (generated)
                      │       ├─▶ a page anyone can ope
                      │       └─▶ one check per decision ──▶ signer
                      └── links to the history for the
```

1. **Capture.** Someone types a rough sentence where the decision is made.
   An assistant formats it and asks one question to set
   ships wrong, is it unlawful or unsafe, or only inconsistent?
2. **Sign.** The function that owns the rule approves t
   is the signature. Repository review rules (`CODEOWNERS`) can enforce it.
3. **Compile.** The folder is validated and compiled in
   agent file gets a short generated block marked "do not edit".
4. **Deliver.** Before building, an agent asks for the
   the components and actions in its plan. It receives a handful, strictest
   first, each with its ID.
5. **Check.** Each decision names a check. Checks run when the design files
   or the code change, and a failure goes to the signer
6. **Review.** On its review date, or earlier if its check fails, a decision
   is renewed, reworded, retired or promoted.
7. **Promote.** A decision that has proved stable becomes a token, a
   statement in a component record, or a lint rule, and

### When two decisions disagree

1. The stricter rank wins.
2. Same rank: the one that names the other in `overrides` wins.
3. Then the narrower scope.
4. Then ask the person who wrote the brief.

Two `MUST`s that conflict are never resolved by the agent. It stops and
names both signers.

### When a decision is unclear in use

The agent reads the justification. If that does not set
designer who launched it to make the call, with one line on why, and
finishes the work. Afterwards it logs the conflict and
work, and flags the entry to the decision's signers. The call applies to
that piece of work only, until the signers confirm, rew

### The agent file

The agent file has two parts. People write the working
things are, which tools to run. The decisions block is generated:

```markdown
<!-- BEGIN GENERATED: decisions — do not edit -->
Before building or changing a component, look up its decisions:
decisions/index.json, filtered by component, flow or ac

Always apply:
- DEC-0004 · MUST — confirm before any action that removes data or
  moves money.
<!-- END GENERATED -->
```

Only decisions that apply to every task appear in the b
fetched by scope.

## Repository layout

```
decisions/          one file per signed decision, plus
decisions/calls/    calls made by designers when a decision was unclear
history/            the full reasoning each decision li
examples/harbor/    the fictional bank used in the experiment
experiment/         protocol, runs and report for Exper
docs/               the concept, the tutorial and the research notes
```

<!-- Adjust this section to match what the repo actuall

## Evidence

One controlled experiment, concluded 5 October 2026. On
same three-screen flow under six briefings, five runs each, with
predictions written down before the first run.

**What held**

- Given the same nine rules, agents with ranked, scoped
  safe path where two rules collided in **9 runs of 10** (10 of 10 counting
  one hidden dialog). Every other briefing managed **0
- The standard rules file named the conflict in its own report in 5 runs of
  5, then built the unsafe option in 5 of 5.
- No out-of-scope decision was applied in any run.

**What did not hold**

- It did not use fewer tokens.
- It did not make runs steadier.
- The test of an unforeseen case was spoiled: the brief leaked the answer.
- The reason and the rank were delivered together, so t
  be separated yet.
- No human rated any output. Quality scores came from a
  judge and are labelled as such.

Under the pre-registered rule the verdict was **adjust**, not go. Limits:
one model, one flow, five runs per condition. Full repo
`experiment/REPORT.md`.

## Status

| Part | Status |
| --- | --- |
| Record format, rank, scope | Tested in Experiment 1 |
| Delivery by scope | Tested in Experiment 1 |
| Generated agent file | Designed |
| Checks on publish | Designed; run by hand once |
| Capture, signing, call logs | Designed |
| Review and promotion | Designed |

Nothing yet shows that people will write and sign decis
records have failed this way before: in one study of projects that adopted
them, about half wrote fewer than five.

## Trying it

Start small, and stop if it does not take.

1. **An afternoon.** Open the file your agents read. Fo
   ask: is this written anywhere a designer would see it, and is it still
   true?
2. **A day.** Write the rules that fail as ranked sentences, one file each.
   Ask the owning function to sign, reword or reject ea
3. **A week.** Generate the agent file block from the folder.
4. **Six weeks.** If nobody has added or changed a deci
   rescue it with more process.

## Credits

Signed Decisions is a concept by Phillip Sanders, developed at Thiga.

It is built to support the component record (CRD) format by **Cassie
Groos**, which holds the rules for a single component.

It borrows from: the Y-statement (Zdun, Capilla, Tran a
architecture decision records (Michael Nygard); RFC 2119 requirement
levels; and studies by Romina Kavcic, Kaelig Deloumeau-
and colleagues, Liu and colleagues, Buchgeher and colleagues, and Jonathan
Grudin. Full references are in `docs/references.md`.

## Licence

Code is MIT. Documentation and the experiment report ar
