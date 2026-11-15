---
name: Button
lifecycle: built
status:
  requirements: complete
  design: complete
  implementation: complete
decisions: [DEC-0004]
---

> A sample written for this repository. The CRD (Component Requirements Document) is the work of
> Cassie Groos, described in her article "Probabilistic isn't a dirty word…" (27 August 2026). This sample
> follows what that article describes; it is not her template.

# CRD: Button

## 1 · Requirements

**Purpose.** Triggers an action with a visible label.

**Anatomy.** Container, label, leading icon, spinner.

### Functional

- F1: The button shows its label in every state except loading.
- F2: The label never wraps onto a second line.

### Integration

- I1: A button that removes data or moves money opens a confirmation dialog; it does not act on the first
  press. (DEC-0004)

### Ruled out

- A second line of label text: every button in a row of actions keeps the same height.

## Decisions

- 2026-09-14: F2. One line keeps every button the same height in a row of actions.
