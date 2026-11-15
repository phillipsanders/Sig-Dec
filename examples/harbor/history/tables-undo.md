# Row actions in tables offer an undo message

- **Date:** 2026-09-14
- **Decision:** DEC-0012
- **Decided by:** design system

In the context of **tables where people manage long lists**, facing a dialog on every row action, we decided
that **row actions take effect at once and offer an undo message**, and neglected a confirmation dialog per
row, to keep list management fast, accepting that a slip stays visible for ten seconds only.

**Limit.** This decision is a SHOULD. Where a row action removes data or moves money, DEC-0004 is stricter
and wins.
