# SigDec Experiment 1 — Report

**Status: concluded, 2026-10-05.** The evidence is automated checks plus an LLM judge with recorded personas, judged blind from screenshots only. **No human raters were used.** Every number derived from persona scores is labelled *LLM-judged*.

**Verdict: ADJUST** (pre-registered rule). H5 held only in part, H6 held, and the stop condition was not met. See §5.

---

## 1. Deviations from the pre-registration (read these first)

1. **No human raters.** The participants were unavailable, so manual scoring was substituted with an LLM judge (`claude-opus-5-5`) playing three recorded personas: A Product Manager, B Lead Product Designer, C Design System Manager (`scoring/personas/`, committed at `5b2fc4d`, before any judging).
   - **Isolation:** one session per pack and pass (3 packs × 3 passes), each in a fresh temp directory containing only the pack PNGs, `card.md` and `persona.md`. Sessions had only Read and Glob, no MCP servers, no skills and no session persistence. Audited: no read outside the folder, and zero Bash calls in all nine sessions.
   - **Record:** pass 1 is the score of record; passes 2–3 measure persona consistency.
   - **No cross-provider check:** no model from another provider was available, so pack B also used `claude-opus-5-5`.
   - **Consequence:** all Q-scores are LLM-judged and indicative. H4, the only hypothesis that depends on a manual score, is deferred.
2. **Annotation pass (secondary, LLM-judged).** Persona R scored each run's redacted annotation text 0/1/2 and never saw a screen. The English annotation panels no longer existed, so the source was the packs' redacted annotation text rather than panel exports.
   - The first run read the files through an auto-approved read-only `head` command. It was re-run with Bash explicitly disallowed; the re-run is the record.
   - The superseded run, which gave every flow 2, is kept for transparency.
3. **Mechanical proxies added post hoc.** P1 (uncovered case) and P2 (conflict) were written into `scoring/rubric.md` as *mechanical proxies, not human judgement*. Two sensitivity checks were also added: A2h and A5h, which count hidden Dialog states. The pre-registered A2 and A5, implemented on visible instances before judging, stay primary.
4. **Hidden states added to the packs.** 8 hidden Dialog and Toast states in 5 runs were exported (clone → visible → export, without modifying the run pages) and added to the packs (`scoring/pack-additions.md`). No export contained annotation layers, decision IDs or condition names.
5. **Run order:** interleaved for round 1 (run 1 of every condition), blocked for runs 2–5 (`predictions.md` § Deviations, `d886191`, `f2e339c`). Run 1 is the only interleaved observation.
6. **Rubric v2:** M1–M3 (0–2 / 0–2 / 1–5) were replaced before any scoring by the Q1–Q3 colour card (1–3 each), at `005ffbf`. H4's M1 threshold is applied to Q1 unchanged, in scale points.
7. **PRD R2.2 leak.** The PRD lists the standing transfer as "set up by the joint account holder", and R2.2 requires showing "who set it up". The "uncovered" case therefore was not fully uncovered: every condition was told the other holder exists. This weakens H4 and the uncovered-case comparison; see §6.
8. **Verdict inputs.** H4 is excluded from the verdict, at the operator's instruction. The verdict uses H5 and H6, with H3 alongside, under the pre-registered go / adjust / stop wording.
9. **Smaller items** (all in `runner/NOTES.md`):
   - C2 run 3's retry was aborted after 16 s and archived; it is not a run.
   - C4 run 1 made two run pages (scored on the final one; X1 flag).
   - C1 run 2 and C4 run 2 wrapped their screens in one frame (X2 flag; they fail the screen-based A-checks, as decided by the operator).
   - Blinding leak: 7 of 42 annotation files quote condition-specific wording verbatim. This is irrelevant to the screenshot judges, who never saw annotations, but relevant to the annotation pass.

## 2. Results

Five runs per condition, `claude-opus-5-5` throughout. A-checks are counts out of 5 (A8 and A10 are totals). P1 and P2 are means on a 0–2 scale.
- **Persona Q1–Q3:** medians of the pass-1 persona scores on a 1–3 scale (7 judgements per condition: 3 personas on the shared run, plus 4 single-judged runs). **LLM-judged.**
- **Annotation:** mean on a 0–2 scale. **LLM-judged.**

| | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 | A2h | A5h | P1 | P2 | Q1 · LLM | Q2 · LLM | Q3 · LLM | Annot. · LLM | drift |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 raw | 4 | 1 | 0 | 4 | 0 | 4 | 5 | 0 | 0 | 1 | 2 | 0 | 1.0 | 0.0 | 2 | 1 | 1 | 1.2 | 4 |
| C2 described | 5 | 0 | 0 | 5 | 0 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1.0 | 0.0 | 2 | 1 | 1 | 1.6 | 0 |
| C3 rules | 5 | 0 | 5 | 5 | 0 | 5 | 2 | 0 | 5 | 0 | 2 | 0 | 1.0 | 0.0 | 2 | 1 | 1 | 2.0 | 0 |
| C4 rich | 4 | 2 | 0 | 4 | 0 | 4 | 4 | 0 | 0 | 1 | 3 | 0 | 1.0 | 0.0 | 2 | 1 | 1 | 2.0 | 4 |
| C5a rich + SigDec | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 0 | 5 | 1 | 5 | 5 | 1.6 | 2.0 | 2 | 3 | 3 | 2.0 | 2 |
| C5b described + SigDec | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 5 | 1 | 5 | 5 | 1.8 | 2.0 | 2 | 3 | 2 | 2.0 | 0 |

Drift = the number of A1–A6 checks that flip across the five runs.

**Cost and tokens** (means per run; `tokens_in` = uncached + cache-creation + cache-read):

| | tokens_in | cache read | cache create | uncached | tokens_out | duration_s | cost_usd |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 410,366 | 374,414 | 35,932 | 20 | 9,538 | 99.2 | 0.60 |
| C2 | 448,714 | 414,237 | 34,455 | 22 | 9,449 | 96.4 | 0.50 |
| C3 | 536,311 | 497,440 | 38,847 | 24 | 12,348 | 126.8 | 0.70 |
| C4 | 588,880 | 543,877 | 44,979 | 24 | 12,758 | 132.5 | 0.70 |
| C5a | 644,361 | 599,291 | 45,043 | 28 | 12,583 | 131.8 | 0.70 |
| C5b | 467,162 | 430,344 | 36,795 | 23 | 10,285 | 107.3 | 0.60 |

Caveat: over 90% of `tokens_in` is cache read, which is driven by turn count and tool-result size (Figma reads), not by the context delivered. With the blocked order, later runs in a block share cache windows. `tokens_in` is a weak proxy for context cost.

## 3. Hypotheses

| # | Prediction (pre-registered) | Observed | Status |
| --- | --- | --- | --- |
| H1 | A1: C2 beats C1 by ≥ 2 runs | C1 4/5, C2 5/5 | **Failed.** C1 already at 4/5; the one miss is the wrapped-frame run (X2) |
| H2 | A3 ≥ 4/5 for C3, C5a, C5b; fails ≥ 4/5 for C1, C2, C4 | 5, 5, 5 vs 0, 0, 0 | **Held** |
| H3 | C3 within 1 run of C5a and C5b on A1, A2, A6 | A1 5/5/5 ✓; A6 5/5/5 ✓; A2 0 vs 4 and 5 ✗ (A2h 2 vs 5/5) | **Failed** (on A2, the closure dialog) |
| H4 | Q1 mean (LLM-judged) C5a ≥ C4 + 1 and ≥ C3 + 1; A4 ≥ 4/5 for C5, ≤ 2/5 for C4 | Q1 mean (LLM-judged): C3 2.00, C4 2.29, C5a 2.43; A4 C4 4/5, C5a 5/5, C5b 5/5 | **Deferred to next run** (LLM-judged, indicative; would not have held) |
| H5 | A5 and A9 ≥ 4/5 for C5a and C5b; A9 ≤ 2/5 for C3 | A5: C5a 4 (A5h 5), C5b 5, C3 0. A9: C5a 5, C5b 5, **C3 5** | **Partly held.** 4 of 5 sub-thresholds met; C3 also named the conflict |
| H6 | A8 = 0 in ≥ 4/5 runs for C5a and C5b | A8 = 0 in all 10 | **Held** |
| H7 | mean tokens_in C5a < C3 | 644k vs 536k (round 1 only: 670,577 vs 608,625) | **Failed** (and confounded by cache; §2) |
| H8 | drift lower for C5a than C1 and C2 | C1 4, C2 0, C5a 2 | **Failed** |
| Null | C4 within 1 of C2 on A1 and A2 | A1 5 vs 4 ✓; A2 0 vs 2 ✗ | **Failed** (C4 drew more closure dialogs than C2) |

## 4. What the persona judge adds (all LLM-judged)

- **Q2 (payee removal) separates the two C5 conditions from the rest.** Median 3 for C5a and C5b, 1 elsewhere (LLM-judged). It agrees 100% with the mechanical proxy P2 across all 42 pack flows. All three personas agreed on Q2 for every shared flow, and every persona's three passes were identical on Q2 (LLM-judged).
- **Q1 (pending transfer) does not separate conditions.** The median is 2 everywhere (LLM-judged). This is consistent with the PRD leak: every condition named the transfer and most said it would be cancelled. Q1 is the least stable judgement: persona C's passes agreed on 57% of flows, and Q1 matched P1 76% (LLM-judged).
- **Q3 (ship it):** median 3 for C5a, 2 for C5b, 1 elsewhere (LLM-judged). This follows the payee-removal protection.

## 5. Verdict

**ADJUST.** Under the pre-registered rule, *go* needs H5 and H6 to hold (H4 is excluded, deviation 8). H6 held. H5 held on four of five sub-thresholds:
- **Both SigDec conditions resolved the conflict** with a confirmation on the bulk payee path: A5 9/10 (10/10 counting a hidden dialog), against 0/20 for C1–C4. They named it in their report 10/10.
- **The failing clause was C3.** The flat rules file also *named* the conflict in 5/5 runs (A9), but resolved it toward the undo toast every time (A5 0/5).
- **Stop doesn't apply.** C3 differs from C5 by more than one run on A2, A5 and A7.

What to adjust follows from the failing clause: the pre-registration assumed flat rules would not even see the conflict. They do see it; what they lack is a way to rank it. Run 2 must separate *rank* from *reason* (§7).

## 6. What can and cannot be claimed

**Can be claimed** (automated checks, n = 5 per condition):
- **Conflict:** given the same nine statements, only the signed-decision conditions put a confirmation on the bulk-removal path: 9/10 runs (10/10 with the hidden state), against 0/5 for the rules file and 0/15 for the metadata conditions. The rules-file runs noticed the clash (A9 5/5) and chose the undo toast.
- **Covered-case metadata result:** danger colour (A1) is right in nearly every run of every condition (4–5/5). A one-sentence description does not measurably beat raw tokens at this ceiling (H1 failed). Rich metadata did not beat described tokens either (A1 4 vs 5).
- **Legal notice availability:** the verbatim notice appears exactly where its text was delivered (C3, C5a, C5b: 5/5) and never elsewhere (0/15). That is a delivery fact, not a format effect.
- **Distractors:** no distractor decision was applied in any C5 run (A8 = 0 in 10/10); scope wording held.

**Cannot be claimed:**
- **Reason vs rank:** C5 delivered both a reason and a strictness rank. The C3 contrast shows the clash was seen without either, but this design can't say which of the two produced the different resolution.
- **Tokens:** H7 failed, and `tokens_in` is dominated by cache reads tied to turn count. No context-cost claim is supported.
- **Uncovered case:** the PRD told every condition who set up the transfer (R2.2 leak). A4 is 4–5/5 everywhere, P1 differs only modestly (C5a 1.6, C5b 1.8 vs 1.0), and the LLM-judged Q1 shows no separation.
- **Human capture:** nothing here measures whether people will write signed decisions, or how long that takes.
- **Human judgement:** no human rated any flow. Persona scores are LLM-judged and indicative.

**Failures and surprises.**
- **Annotation-only fixes:** C1–C4 agents often *listed* a payee-removal confirmation among their invented decisions (2–5 of 5 runs per condition) but placed none on the page. The X3 flag records the same pattern: a dialog described in an annotation, never built.
- **Recurring inventions across all conditions:** "transfer cancelled at closure" (3–5 of 5 runs everywhere), and a placeholder for the legal notice wherever its text wasn't delivered.
- **The agents annotate generously:** the annotation pass gave 2 to 24 of 30 runs (LLM-judged), so it barely separates conditions (1.2 for C1 to 2.0 for C3–C5).

## 7. Pre-registered changes for run 2

1. **Brief without the joint-holder fact.** Remove "set up by the joint account holder" and the "who set it up" clause from R2.2, so the uncovered case really is uncovered.
2. **Add a condition "RFC 2119 rules without reasons":** the nine statements as MUST / SHOULD / MAY with ranks but no reasons, to separate rank from reason (§5).
3. **Token reporting with the cache split** (uncached / cache-create / cache-read) and turn count. Optionally normalise by turns; pre-register the token hypothesis on uncached + cache-create only.
4. **Delivered-set hash in the closing JSON:** the agent reports a hash of the decision or rule set it read, so A7 can be verified mechanically.
5. **Human raters budgeted,** or the LLM judge (model, personas, passes, card) pre-registered as the measure before any run.
6. **Log every tool call** in generation runs (`--output-format stream-json --verbose`), so file reads, decision files opened, `$extensions` / variable-description look-ups and Figma MCP calls can be counted per run.
7. **Already fixed in the tooling:** count hidden states in A2/A5 (pre-register A2h/A5h), forbid Bash in judge sessions, and keep the order interleaved throughout.

## Appendix

**Manifest.** `runner/results/manifest.json`:
- model `claude-opus-5-5`; BASE `zFwo5GgtfaZ3jIzIdCU90U`;
- condition files: C1 `jrjRslqzInEYcmaKPvLlWE`, C2 `Utlgnw9Mzi2ViAXBJ4s1o2`, C3 `qLya4xeDTKU3kp7mBXgpoJ`, C4 `jIR8kxG0HqsZId4zh5lO2g`, C5a `YDzHTHlaYoAVLPZ9cqjh4K`, C5b `zQorssSKYwXyf04Jm98HIt`;
- `started_at` 2026-10-02T09:05:48Z; `run_order` blocked (round 1 interleaved).

**Model IDs.** Generation and judging used `claude-opus-5-5` only.

**Key commits.**
- Pre-registration: `3d6605e`, then deviations at `d886191`, `f2e339c` and `005ffbf` (current `predictions_commit`).
- Personas: `5b2fc4d`.
- Judging: `980c990`.
- Annotation pass: `6adb0da` (superseded), `251eab7` (record).
- Proxies and pre-unseal inference: `99b6afb`.
- Agreement: `4059b73`.

**Personas and their consistency** (LLM-judged; `scoring/agreement.md`):

| Persona | File | Pass-to-pass identical: Q1 / Q2 / Q3 |
| --- | --- | --- |
| A · Product Manager | `scoring/personas/A.md` | 100% / 100% / 100% |
| B · Lead Product Designer | `scoring/personas/B.md` | 100% / 100% / 93% |
| C · Design System Manager | `scoring/personas/C.md` | 57% / 100% / 93% |
| R · Reviewer (annotations only) | `scoring/personas/R.md` | single pass; the superseded run differed on 6/30 flows |

On the 6 shared flows, all three personas agreed on Q1 67%, Q2 100% and Q3 67% (persona consistency, LLM-judged; not inter-rater reliability).

**Proxy rules.** See `scoring/rubric.md`, sections "Mechanical proxies — not human judgement" and "Sensitivity checks".

**Pack additions.** See `scoring/pack-additions.md`: 5 pack flows gained hidden-state PNGs (4 in pack A, 4 in pack C).

**Seal cross-check.** The condition inference recorded before unsealing from annotation markers (`scoring/inference-preunseal.md`) matched the map on 41 of 42 pack flows. The one miss was a C3 flow marked "unclear (ref without level)": pack C, `36835b3450` (C3 run 4).

## Process metrics (recoverable after the fact)

Means per run. Per-run values are in `scoring/process_metrics.csv` (`scoring/process_metrics.py`).

| | Thinking tokens | API time (s) | Tool time (s) | Time to first token (s) | Refused tool calls | IDs applied | Conflicts flagged | Analogies flagged | Items invented | Nodes on page | Annotations | Component instances | Dialog instances | Button instances |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2,095 | 97.7 | 1.5 | 2.5 | 0 | 0 | 0 | 0 | 9.8 | 90.8 | 10.6 | 17 | 0.4 | 6.8 |
| C2 | 1,758 | 94.7 | 1.7 | 3.1 | 0 | 0 | 0 | 1 | 10.2 | 82 | 9.8 | 15.4 | 0 | 5.8 |
| C3 | 4,396 | 125.1 | 1.7 | 2.1 | 0 | 7.8 | 1.4 | 1.6 | 9.6 | 80.2 | 11 | 15.8 | 0.4 | 6 |
| C4 | 3,012 | 124.7 | 7.7 | 2.0 | 0 | 3 | 1.4 | 2.4 | 9 | 84.4 | 11.4 | 16.2 | 0.6 | 7 |
| C5a | 3,300 | 129.2 | 2.6 | 2.3 | 1.8 | 4 | 1 | 0.4 | 9.8 | 96.4 | 13.2 | 20.6 | 2 | 9.8 |
| C5b | 2,228 | 105.7 | 1.7 | 2.6 | 1 | 4 | 1 | 0.4 | 8 | 99.8 | 11.8 | 22 | 2 | 10.6 |

**Reading these:**
- **Time is model time.** Tool time (agent time minus API time, including every Figma call) averages 1.5–7.7 s of a 95–132 s run, so condition differences in duration come from model reasoning and output, not from fetching context.
- **Decisions applied.** Across the 10 C5 runs the agents cited only DEC-0004, DEC-0007, DEC-0023 and DEC-0031 (C5a DEC-0004 ×5, DEC-0007 ×5, DEC-0023 ×5, DEC-0031 ×5; C5b DEC-0004 ×5, DEC-0007 ×5, DEC-0023 ×5, DEC-0031 ×5). DEC-0012 (undo toast), the losing side of the conflict, was never applied, and no distractor was cited (H6).
- **Refused tool calls occur only in C5 runs** (C5a 5/5, C5b 5/5). They are Bash commands, which the run had no permission for, trying to `cat` decision files and `components.md` and to print every token's `$description`. The refused commands name DEC-0004, DEC-0007, DEC-0012, DEC-0023, DEC-0031 (C5a) and DEC-0004, DEC-0007, DEC-0012, DEC-0019, DEC-0023, DEC-0031 (C5b). How they then read them isn't logged; that they did is shown by every C5 run citing the decisions' IDs. C5b runs also tried to open the distractor DEC-0019, and both conditions tried DEC-0012, yet neither was applied. This is a lower bound on what agents tried to read, not a count.
- **IDs applied outside C5:** C3 cites UX.md rules (7.8 per run); C4's non-zero count is run 3 listing kit components and tokens (the A7 failure). Neither cites a DEC ID.
- **Kit usage:** C5 runs place more instances (20.6 and 22 per run against 15.4–17), mostly extra Buttons and the 2 Dialogs (closure + payee removal) behind A2 / A5.

**Not recoverable from this run:**
- The generations used `--no-session-persistence` with `--output-format json`, which keeps only the final result, so there is no per-tool-call record.
- The following can't be counted after the fact:
  - the number of file reads or Glob calls per generation (requests to the condition folder);
  - which files were read, including whether a run opened `sigdec/INDEX.md` or individual decision files;
  - how often `tokens.json` (and its `$extensions`) or the Figma variable descriptions were consulted;
  - the number of Figma MCP calls by tool.
- The judge and annotation sessions did log every call (stream JSON); their counts are in §1 and the judge logs.
- **Run 2 change:** run each generation with `--output-format stream-json --verbose`, saved next to `result.json`. Every Read, Glob and MCP call is then logged with its arguments, so file reads, `$extensions` look-ups, decision files opened and Figma calls per run can be counted and joined to the outcome checks.

## Per-generation tokens and time

One row per generation run, including the trial and the aborted retry. Values come from each run's `claude -p` result JSON (`runner/collect.py` → `runner/results/runs.csv`); none was typed by hand.
- **Tokens:** `tokens_in` = uncached input + cache creation + cache read.
- **Agent time:** the session duration reported by `claude -p`.
- **Wall time:** measured by the runner around the whole call, including start-up.

| Condition | Run | Status | Turns | tokens_in | uncached | cache create | cache read | tokens_out | Agent time (s) | Wall time (s) | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1-raw | 0 | trial (not counted) | 12 | 366,022 | 18 | 34,144 | 331,860 | 9,241 | 88.5 | 90 | 0.52 |
| C1-raw | 1 | counted | 13 | 427,092 | 20 | 37,686 | 389,386 | 10,347 | 103.4 | 105 | 0.59 |
| C1-raw | 2 | counted | 11 | 357,260 | 16 | 42,827 | 314,417 | 9,627 | 106.8 | 109 | 0.60 |
| C1-raw | 3 | counted | 15 | 506,663 | 26 | 30,904 | 475,733 | 9,227 | 98.1 | 99 | 0.53 |
| C1-raw | 4 | counted | 11 | 314,887 | 16 | 32,716 | 282,155 | 8,721 | 85.9 | 87 | 0.49 |
| C1-raw | 5 | counted | 14 | 445,930 | 22 | 35,528 | 410,380 | 9,770 | 101.7 | 103 | 0.56 |
| C2-described | 1 | counted | 12 | 409,329 | 20 | 34,597 | 374,712 | 10,768 | 98.5 | 101 | 0.57 |
| C2-described | 2 | counted | 10 | 391,830 | 20 | 35,063 | 356,747 | 9,232 | 97.1 | 98 | 0.54 |
| C2-described | 3 | counted | 16 | 556,852 | 26 | 36,096 | 520,730 | 10,381 | 108.5 | 110 | 0.60 |
| C2-described | 3b | aborted retry (not counted) | — | — | — | — | — | — | — | 16 ¹ | — |
| C2-described | 4 | counted | 11 | 403,729 | 20 | 33,948 | 369,761 | 7,680 | 82.4 | 84 | 0.50 |
| C2-described | 5 | counted | 15 | 481,829 | 24 | 32,571 | 449,234 | 9,186 | 95.5 | 97 | 0.53 |
| C3-rules | 1 | counted | 16 | 608,625 | 28 | 38,198 | 570,399 | 13,074 | 132.4 | 134 | 0.68 |
| C3-rules | 2 | counted | 13 | 487,932 | 22 | 40,261 | 447,649 | 11,769 | 125.3 | 128 | 0.65 |
| C3-rules | 3 | counted | 12 | 469,635 | 22 | 38,149 | 431,464 | 11,421 | 116.1 | 118 | 0.62 |
| C3-rules | 4 | counted | 15 | 643,062 | 28 | 41,278 | 601,756 | 15,414 | 155.7 | 157 | 0.76 |
| C3-rules | 5 | counted | 13 | 472,302 | 22 | 36,348 | 435,932 | 10,061 | 104.6 | 106 | 0.58 |
| C4-rich | 1 | counted | 18 | 933,261 | 36 | 49,472 | 883,753 | 18,746 | 198.5 | 200 | 0.95 |
| C4-rich | 2 | counted | 13 | 466,794 | 20 | 46,074 | 420,700 | 11,171 | 114.3 | 117 | 0.68 |
| C4-rich | 3 | counted | 14 | 588,646 | 24 | 46,298 | 542,324 | 12,946 | 127.7 | 129 | 0.74 |
| C4-rich | 4 | counted | 10 | 454,627 | 20 | 42,185 | 412,422 | 9,853 | 103.6 | 106 | 0.62 |
| C4-rich | 5 | counted | 13 | 501,071 | 22 | 40,865 | 460,184 | 11,073 | 118.2 | 119 | 0.64 |
| C5a-rich-sigdec | 1 | counted | 18 | 670,577 | 28 | 51,552 | 618,997 | 14,040 | 148.6 | 151 | 0.82 |
| C5a-rich-sigdec | 2 | counted | 17 | 540,092 | 28 | 35,338 | 504,726 | 12,443 | 125.6 | 127 | 0.63 |
| C5a-rich-sigdec | 3 | counted | 22 | 563,400 | 24 | 43,945 | 519,431 | 12,225 | 121.0 | 123 | 0.70 |
| C5a-rich-sigdec | 4 | counted | 15 | 529,708 | 24 | 43,087 | 486,597 | 10,703 | 120.2 | 122 | 0.66 |
| C5a-rich-sigdec | 5 | counted | 19 | 918,030 | 36 | 51,292 | 866,702 | 13,504 | 143.5 | 145 | 0.85 |
| C5b-described-sigdec | 1 | counted | 14 | 455,675 | 22 | 37,720 | 417,933 | 10,948 | 121.2 | 123 | 0.60 |
| C5b-described-sigdec | 2 | counted | 11 | 402,795 | 20 | 36,367 | 366,408 | 9,980 | 102.6 | 105 | 0.56 |
| C5b-described-sigdec | 3 | counted | 15 | 498,657 | 24 | 36,832 | 461,801 | 10,533 | 109.9 | 112 | 0.60 |
| C5b-described-sigdec | 4 | counted | 16 | 484,650 | 24 | 34,990 | 449,636 | 9,146 | 95.2 | 97 | 0.55 |
| C5b-described-sigdec | 5 | counted | 16 | 494,032 | 24 | 38,066 | 455,942 | 10,818 | 107.8 | 110 | 0.61 |
| **Counted runs (30)** | | | | **15,478,972** | | | | **334,807** | **3470** (57.8 min) | **3522** (58.7 min) | **19.00** |
| **All generation runs (32)** | | | | **15,844,994** | | | | **344,048** | **3558** | **3628** | **19.53** ² |

¹ Stopped by the orchestrator 16 s after start (09:55:07Z → 09:55:23Z), before `claude -p` returned. No result JSON was written, so no token, turn or cost data exist. Any tokens it consumed in those 16 s are unrecorded.
² Excludes the aborted retry's unrecorded usage. The first trial attempt never started `claude` (run.sh path bug), so it used no tokens.

## Scoring-session tokens and time

One row per LLM-judge session (step 3) and annotation session (step 4), from the `result` line of each `scoring/judge-logs/*.txt` stream. Agent time is the duration reported by `claude -p`; the judge runner did not time these sessions separately, so there is no wall time.

| Session | Purpose | Turns | tokens_in | uncached | cache create | cache read | tokens_out | Agent time (s) | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-pass1 | persona A, pass 1 (score of record) | 55 | 1,092,438 | 34 | 88,027 | 1,004,377 | 7,306 | 86.9 | 1.05 |
| A-pass2 | persona A, pass 2 | 55 | 1,091,782 | 34 | 87,866 | 1,003,882 | 7,193 | 136.6 | 1.05 |
| A-pass3 | persona A, pass 3 | 55 | 1,089,159 | 34 | 87,748 | 1,001,377 | 7,050 | 94.2 | 1.04 |
| B-pass1 | persona B, pass 1 (score of record) | 57 | 1,123,327 | 34 | 91,399 | 1,031,894 | 8,273 | 91.9 | 1.10 |
| B-pass2 | persona B, pass 2 | 57 | 1,124,315 | 34 | 91,524 | 1,032,757 | 8,303 | 92.5 | 1.10 |
| B-pass3 | persona B, pass 3 | 57 | 1,123,813 | 34 | 91,478 | 1,032,301 | 8,263 | 95.3 | 1.10 |
| C-pass1 | persona C, pass 1 (score of record) | 59 | 928,413 | 30 | 89,919 | 838,464 | 8,564 | 95.7 | 1.06 |
| C-pass2 | persona C, pass 2 | 59 | 926,174 | 30 | 89,108 | 837,036 | 7,713 | 87.3 | 1.03 |
| C-pass3 | persona C, pass 3 | 59 | 930,063 | 30 | 89,667 | 840,366 | 8,293 | 100.9 | 1.05 |
| R-annotations.superseded-bash | annotation pass (superseded, Bash) | 7 | 207,523 | 14 | 34,165 | 173,344 | 2,617 | 40.4 | 0.36 |
| R-annotations | annotation pass (record) | 33 | 153,001 | 10 | 34,292 | 118,699 | 5,109 | 52.9 | 0.40 |
| **All scoring sessions (11)** | | | **9,790,008** | | | | **78,684** | **975** (16.2 min) | **10.36** |

**Data.**
- Per-condition figures: `scoring/results.json`.
- Joined inputs: `runner/results/runs.csv`, `scoring/checks.csv`, `scoring/manual-{A,B,C}.csv` (+ `.pass2` / `.pass3`), `scoring/annotations-judge.csv`.
- Seals: `scoring/.sealed/` (now public).
