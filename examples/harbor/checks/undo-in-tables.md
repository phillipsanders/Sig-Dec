# undo-in-tables

- **Decision:** DEC-0012
- **Reads:** the Figma file of the flow under test (read-only)

## Steps

1. Find every data table and list its row actions and bulk actions.
2. Leave out any action covered by DEC-0004 (it removes data or moves money): that check decides it.
3. Pass if the remaining actions show an undo message and no dialog.

## Report

One line per action: table, action, pass or fail.
