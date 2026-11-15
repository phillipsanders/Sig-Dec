# Harbor design system: context for agents

## Where things are

- `tokens/` holds the design tokens. Values are authoritative in the Figma library.
- `crd/` holds one CRD per component. Read the record before changing a component.
- `decisions/` holds the rules that cross components. Do not edit `decisions/index.json` or the block below.

## Working rules

- Change nothing in Figma without an explicit request. Reviews and checks are read-only.
- The scope of a task is the list you were given. Propose additions in one sentence; do not make them.
- If a decision is unclear for the work in hand, read its justification. If it is still unclear, ask the
  person who launched you to make the call, then log it in `decisions/calls/`.
- If two MUST decisions conflict, stop and name both signers.

<!-- BEGIN GENERATED: decisions — do not edit; run sigdec.py compile -->
Before building or changing a component, look up its decisions:
decisions/index.json, filtered by component, flow or action
(or run `sigdec.py scope <keys>`).

Always apply:
- DEC-0004 · MUST — Any action that removes data or moves money MUST confirm first.
- DEC-0042 · MUST — An icon-only button MUST have an accessible name.
<!-- END GENERATED -->
