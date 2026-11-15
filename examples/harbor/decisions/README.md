# decisions/

One file per signed decision. A decision is a rule that more than one component or flow must follow.

- A rule about one component belongs in that component's CRD (`crd/`), which cites the decision ID
  when it depends on one.
- A value belongs in a token.
- The reasoning belongs in `history/`. Each decision links to it.

Write a decision only if someone could plausibly propose the opposite. Keep values out of the sentence.

## Rank

Set by what breaks if the decision ships wrong.

| Rank | When | Review |
| --- | --- | --- |
| MUST | law, money, safety or accessibility | every year |
| SHOULD | the product becomes inconsistent | after twelve months |
| MAY | a working arrangement | expires after ninety days |

The first line of the record contains exactly one of these words, in capitals.

## When two decisions disagree

1. The stricter rank wins.
2. Same rank: the one that names the other in `overrides` wins.
3. Then the narrower scope.
4. Then ask the person who wrote the brief.

Two MUSTs that conflict are never resolved by an agent. It stops and names both signers.

## Status

`proposed` (not delivered to agents) → `accepted` → `promoted` (now a token, a CRD statement or a lint
rule; no longer delivered) or `retired`. A declined draft moves to `rejected/` with the reason.

## Fields

| Field | Required | Meaning |
| --- | --- | --- |
| `id`, `status`, `rank` | yes | as above |
| `scope` | yes | keys from `scopes.txt`: `component:`, `flow:`, `action:`, `content:`, `state:` |
| `decision-makers` | yes | the functions that sign, never a person |
| `date`, `review` | review | when it was signed; when it is looked at again (`YYYY-MM`) |
| `justification` | no | a path into `history/`, or `pending` |
| `verify` | no | a file in `checks/`, or `axe:<rule>` / `lint:<rule>` |
| `overrides` | no | the decision this one replaces or is an exception to |
| `always` | no | `true` puts the decision in the agent file block |
| `reader` | no | `product` or `system` |
| `promoted-to` | when promoted | where the rule lives now |
