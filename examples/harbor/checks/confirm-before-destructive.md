# confirm-before-destructive

- **Decision:** DEC-0004
- **Reads:** the Figma file of the flow under test (read-only)

## Steps

1. List every interactive element whose label or name contains: delete, remove, close account, cancel
   transfer, send, pay, transfer.
2. For each one, follow its prototype link or the next frame in the flow.
3. Pass if the next thing shown is a dialog whose text names the consequence (what is removed, or the
   amount and the recipient).
4. Fail if the action completes directly, or if the only safeguard is an undo message.

## Report

One line per element: frame, element, pass or fail, and what follows the press. Count hidden dialogs
separately: a dialog that exists but is not connected is a fail with a note.
