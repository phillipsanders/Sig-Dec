# SigDec research protocol: theory, experiment and success criteria

Oct 2, 2026 · @Phillip

This protocol fixes the claim, the test and the pass/fail thresholds before any generation is run, so the result can be read without arguing about what it means afterwards.

## Thesis

An AI generating UI from a design system follows the rules it is given, but when it meets a case no rule covers it guesses. We claim that giving it the *decision* behind a rule, in one sentence that keeps the reason, a strictness and a scope, lets it extend correctly to the uncovered case and resolve conflicts consistently, where the same content written as metadata or flat rules does not. We also claim that delivering decisions scoped to the task costs no more input tokens than loading a rules file.

The claim is falsified if, with identical content, the decision form performs no better than flat rules or rich metadata on the uncovered case and on the conflict case. In that event the machine-side argument for SigDec is withdrawn and the concept rests only on its human side (capture by whoever decides, authorship, lifecycle), which this experiment does not test.

> **One sentence for the sceptic.** Metadata tells the model what we decided; it cannot tell the model why, who, or until when, and those are what it needs when it meets a case we did not foresee. This experiment checks whether that is true, or just plausible.

## Background and gap

The design-system field has solved delivery to machines and left origination to developers.

- **Delivery works.** 18 of 21 open-source systems in Kaelig Deloumeau-Prigent's July 2026 study ship an MCP server; validation loops appear in all 21; tool-gating (making the wrong answer impossible) outperforms prohibition ([study](https://state-of-ai-in-design-systems.netlify.app/)).
- **Meaning on tokens helps.** Romina Kavcic's audit of 50 token files found 1 that said what a token must not be used for; one sentence per token fixed the brand-red-on-delete error in her test ([audit](https://aidesign.guide/token-audit)).
- **Long instruction files do not.** Gloaguen et al. (2026, arXiv:2602.11988) found AGENTS.md-style files gave no general improvement and raised cost by over 20 %; Liu et al. (2023) documented retrieval loss in the middle of long contexts.
- **Nobody records who decided or why.** Primer links review rules to decision records, the closest precedent, but in a contributor folder, for review only, by developers. No system reviewed gives a rule an owner, an expiry or a front door for the people who originate decisions.

The gap this experiment addresses is narrower than the concept: not *who writes* the rule, but whether the *form* of the rule, when it carries its reason, strictness and scope, changes what the machine does on cases the rule did not foresee.

## The concept under test

SigDec is a folder of one-sentence design decisions, each in the Y-statement shape (*in the situation X, facing Y, we decided Z, to achieve A, accepting B*) plus four things metadata does not carry: a concrete "Not this" example, the name and role of whoever decided, a strictness (working, binding, mandatory) and dates for review or expiry.

The folder is not a rival to tokens or component metadata. It is the step before them: decisions are captured where they are made, delivered scoped to whatever an agent or designer touches, checked where a check exists, and promoted into a token, a component constraint or a lint rule once they prove stable. The measure of a healthy folder is that it shrinks.

| Layer | Holds | Who writes it today | What this experiment varies |
| --- | --- | --- | --- |
| Tokens (bare → described → rich DTCG) | values, roles, use / do-not-use, scopes | design system team | C1, C2, C4 |
| Flat rules (AGENTS.md, UX.md) | imperatives, no reason, no owner | developers | C3 |
| SigDec | the same statements with reason, strictness, scope, signer, dates | whoever decided | C5a, C5b |
| Component code, lint, CI | promoted decisions | developers | not varied (destination) |

Only the middle two rows differ in form between conditions. The content, nine statements about the Harbor banking app, is held constant.

## Research questions and hypotheses

Three questions, eight hypotheses. Each hypothesis names the comparison that decides it and the result that would count against it.

**RQ1. Does meaning on tokens help, and how far does it go?** (replication and ceiling)

**RQ2. With identical content, does the decision form change behaviour on cases the rules did not foresee?** (the core claim)

**RQ3. Does scoped delivery of decisions cost less than loading a rules file?** (the efficiency claim)

| ID | Hypothesis | Decided by | Falsified if |
| --- | --- | --- | --- |
| H1 | Described tokens beat raw tokens on the danger-colour check (A1). | C1 → C2 | C2 passes A1 in no more runs than C1 |
| H2 | Rules with no token to live on (the legal notice, A3) are followed only where the text is available. | C1, C2, C4 vs C3, C5 | C1/C2/C4 pass A3 in ≥ 2 of 5 runs (they would be inventing it) |
| H3 | With equal content, flat rules and decisions tie on the covered checks (A1, A2, A6). | C3 ≈ C5a/C5b | a gap of more than one run on any covered check |
| H4 | On the uncovered case (pending transfer), decisions beat both rich metadata and flat rules. | C4 → C5a, C3 → C5b | mean M1 for C5 < C4 + 1.0 or < C3 + 1.0, or A4 passes in fewer than 4 of 5 C5 runs |
| H5 | On the conflict (table undo vs confirm first), a strictness label gives the same outcome every run; flat rules do not. | C3 vs C5 on A5, A9 | C5 passes A5 in fewer than 4 of 5, or C3 passes in 3 or more |
| H6 | Scoped decisions are not over-applied. | A8 in C5 | any distractor ID applied in 2 or more C5 runs |
| H7 | Scoped delivery costs fewer input tokens than a whole rules file. | C5a vs C3 tokens\_in | C5a mean tokens\_in ≥ C3 mean tokens\_in |
| H8 | Decisions reduce drift across repeated runs. | flips of A1–A6 across 5 runs | C5a flips as many or more checks than C1 or C2 |

H3 is a hypothesis of *no difference* and is as important as H4: if decisions beat rules on the easy cases too, the gain is probably coming from something other than the reason, such as prompt length or salience, and the design is confounded.

**Null result expected on one comparison.** C4 (rich DTCG metadata) is predicted to perform like C2 on the covered checks. If it does, rich metadata adds little once a role is described in a sentence; if it beats C2 on the uncovered case, the manager's position gains support and should be reported as such.

## Method

A between-conditions design: six conditions, one task, five fresh runs each, 30 generations on one pinned model, executed headlessly so that tokens, duration and model are read from the run result and never typed by hand. The full build and run procedure is `EXPERIMENT_PROMPT.md` in the repository.

**Conditions** (same Harbor UI kit, same PRD, same task prompt; only the context differs)

| Condition | Tokens | Rules | SigDec | Represents |
| --- | --- | --- | --- | --- |
| C1-raw | values only | — | — | an undocumented system |
| C2-described | + one sentence per token | — | — | Kavcic's fix |
| C3-rules | described | AGENTS.md + UX.md (parity) | — | the field's format |
| C4-rich | + do-not-use, $extensions, scopes, code syntax | — | — | metadata done properly (the manager's position) |
| C5a-rich-sigdec | rich | — | index + files, fetched by scope | SigDec on top of the strongest metadata |
| C5b-described-sigdec | described | — | same | SigDec with modest metadata |

**Task.** Generate a three-screen "Close savings account" flow in Figma from a neutral PRD. The PRD contains the data that makes three probes possible without naming any of them: a destructive final action (covered), a €450 standing transfer to the joint account holder that no rule mentions (uncovered), and bulk removal of payees in a table, where "tables use undo" meets "destructive actions confirm first" (conflict).

**Content held constant.** Nine statements: five tested (confirm first, two reds, verbatim legal notice, tables use undo, empty states offer an action) and four distractors out of scope for this flow. They appear once as SigDec files with reasons, signers, strictness and scope, and once in UX.md as bare imperatives in the same order. C1, C2 and C4 receive neither.

**Measures.** Ten automated checks read from the Figma file through the REST API (danger variable bound, dialog before closure, legal text exact, pending transfer named, bulk removal confirmed, empty-state button, cited IDs exist and were delivered, distractors applied, conflict named, hard-coded hex count); three blind manual scores on hashed screenshots (uncovered-case handling 0–2, annotation quality 0–2, plausibility 1–5); and from each run's JSON result: input tokens including cache, output tokens, duration, turns, cost, model.

**Controls.**

- One Figma file per condition and one leaf directory per condition, copied outside the repository before each run; the run can read nothing else.
- No `CLAUDE.md` anywhere except inside the C3 directory; tools limited to the Figma MCP plus read-only file access.
- Byte-identical task prompt apart from the list of files present.
- Interleaved order (run 1 of every condition, then run 2…) so model-side drift over the session does not land on one condition.
- Predictions committed before the first run; the commit hash is recorded with the results.
- Every cited decision ID is checked against the set that condition actually received; an ID never provided counts as a failure.

**Size.** 30 runs is enough to see effects of the predicted magnitude (a 2-run gap out of 5 on binary checks, a 1-point gap on M1) and to detect drift; it is not enough for inferential statistics, and none will be reported.

## Success and failure criteria

The verdict is read off H4, H5 and H6, with H3 as a validity gate. It is decided here, before the runs.

| Verdict | Condition | What it means for SigDec |
| --- | --- | --- |
| **Go** | H4 and H5 hold; H6 holds; H3 holds (no gap on covered checks) | The reason and the strictness do work the metadata and rules cannot. Proceed to the five-day study and to the human-side test (capture by non-developers). |
| **Adjust** | Exactly one of H4 / H5 holds, or H6 fails (distractors applied), or H3 fails (decisions also win the easy cases) | The effect exists but the mechanism is unclear or the scope wording leaks. Fix the named cause, re-run only the affected conditions, do not widen the claim. |
| **Stop** | Neither H4 nor H5 holds: C5a ≈ C4 and C5b ≈ C3 on the uncovered and conflict probes | The form of the rule does not change machine behaviour. Withdraw the machine-side claim. SigDec may still be worth running for its human side, but that is a different experiment and a different pitch. |

Two results are reported whatever the verdict: H7 (token cost) as a measured number with its cache caveat, and the C2 → C4 comparison, which is the manager's position tested on its own terms.

**Ties go against the claim.** Where a threshold is met exactly, the hypothesis is recorded as *inconclusive* and counts as not held for the verdict.

## Expected outcomes

Predicted pass counts out of 5 runs, and predicted mean manual scores, per condition. These are the numbers the results table will be laid beside; they are commitments, not estimates to be revised after the fact.

| Check | C1 raw | C2 described | C3 rules | C4 rich | C5a rich + SigDec | C5b described + SigDec |
| --- | --- | --- | --- | --- | --- | --- |
| A1 danger variable bound | 1 | 4 | 5 | 5 | 5 | 5 |
| A2 dialog before closure | 3 | 3 | 5 | 5 | 5 | 5 |
| A3 legal notice exact | 0 | 0 | 5 | 0 | 5 | 5 |
| A4 pending transfer named | 1 | 1 | 2 | 2 | 4 | 4 |
| A5 bulk removal confirmed | 2 | 2 | 2 | 3 | 4 | 4 |
| A6 empty state has button | 3 | 3 | 5 | 4 | 5 | 5 |
| A8 distractors applied (count) | — | — | 1 | — | 0 | 0 |
| A9 conflict named | 0 | 0 | 1 | 0 | 4 | 4 |
| M1 uncovered case (0–2) | 0.4 | 0.4 | 0.8 | 1.0 | 1.8 | 1.6 |
| M2 annotation quality (0–2) | 0.6 | 0.8 | 1.4 | 1.2 | 1.8 | 1.8 |
| tokens\_in, relative to C3 | 0.7× | 0.7× | 1.0× | 0.9× | 0.8× | 0.75× |
| drift: checks that flip across runs | 4 | 3 | 2 | 2 | 1 | 1 |

How to read the table against the hypotheses: H1 is the C1 → C2 jump on A1; H2 is the zero row for A3 wherever the text was not supplied; H3 is C3 and C5 agreeing on A1, A2, A6; H4 is the A4 and M1 gap between C4 and C5a; H5 is the A5 and A9 gap between C3 and C5; H7 is the last-but-one row; H8 the last.

The weakest prediction is A5 for C4. Rich component metadata may legitimately say "danger buttons open a confirmation", which could carry the bulk-removal case without any strictness label. If C4 reaches 4 or 5 on A5, that is a real point for metadata and should be written up as one.

## Threats to validity and known asymmetries

| Threat | Direction | Mitigation |
| --- | --- | --- |
| **Leakage between conditions** through Figma variables, parent `CLAUDE.md` files or shared directories | inflates weaker conditions | one file and one leaf directory per condition, runs from a temp copy, `VERIFY.sh` fails the build on any stray file |
| **Prompt-length confound**: C5 prompts are longer, so gains could come from salience, not reason | inflates C5 | H3 is the gate: if C5 also beats C3 on the easy checks, the gain is suspect |
| **Legal notice asymmetry**: C1, C2 and C4 are not given the notice text at all, so A3 tests availability, not form | penalises C4 | report A3 as an availability result (H2), not as a C4 → C5 difference; note that a DS team *could* hold the text in a component description |
| **Rich metadata can state behaviour** ("danger buttons confirm") and may carry the conflict case without a strictness label | favours C4 on A5 | predicted and welcomed; a C4 win on A5 is reported as support for the manager's position |
| **Scorer bias** on the manual rubric | any direction | hashed screenshots, sealed map, second scorer on a 20 % sample |
| **Model drift across the session** | any direction | interleaved order, pinned model ID recorded per run |
| **Token counts depend on prompt caching** | obscures H7 | report cache-read and cache-create separately; compare uncached input where possible |
| **MCP bridge instability**: a failed run is not a failed condition | adds noise | failed runs recorded and re-run once as `run Nb`, never dropped |
| **The task is one flow in one domain** | limits generality | stated as a limit; the five-day study widens it |
| **The author designed the probes** | favours the claim | predictions committed first; thresholds set so a tie counts against the claim |

## What the experiment cannot tell us

It tests the machine side only. Three parts of the concept are untouched:

- **Capture.** Whether PMs, designers and Legal will write a decision in ten seconds, and keep doing it after six weeks. That is the one-day capture check and the Level 1 field test, not this study.
- **Lifecycle.** Whether decisions actually get promoted and the folder shrinks. That needs months of a real team.
- **Model generality.** One pinned model. A small local model is an optional extension (H7 of the five-day plan), not part of this run.

A *go* here means the form of a decision changes what a machine does with it. It does not yet mean a team will write them.
