---
name: Data table
lifecycle: active
status:
  requirements: complete
  design: in progress
  implementation: not started
decisions: [DEC-0004, DEC-0012, DEC-0042]
---

> A sample written for this repository. The CRD (Component Requirements Document) is the work of
> Cassie Groos, described in her article "Probabilistic isn't a dirty word…" (27 August 2026). This sample
> follows what that article describes; it is not her template. The `decisions:` field and the IDs in
> brackets are additions made here.

# CRD: Data table

## 1 · Requirements

**Purpose.** Shows a list of records in rows, and lets people act on one row or on several.

**Scope.** In: sorting, row actions, bulk actions. Out of scope: editing a value inside a cell, which
belongs to the editable table.

**Anatomy.** Container, header row, row, cell, row action, bulk action bar, undo message.

### Behaviour

- B1: A row action takes effect at once and shows an undo message. (DEC-0012)
- B2: A row action that removes data or moves money opens a confirmation dialog first; it never uses an
  undo message. (DEC-0004)
- B3: A bulk action follows the same rule as the row action it repeats. (DEC-0004, DEC-0012)
- [open] B4: Archiving a row is treated as reversible. Waiting for the signers of DEC-0004.

### Accessibility

- A1: Every icon-only row action has an accessible name. (DEC-0042)
- [review] A2: The undo message stays long enough to be read and reached with a keyboard.

### Ruled out

- A confirmation dialog on every row action: it slows down people who manage long lists.

### Open questions

- Does archiving a payee count as removing data? Waiting on product and legal. A call was logged on 15/11.

## Decisions

- 2026-11-15: B2 is split from B1, because delete and payments follow DEC-0004, which is stricter.
