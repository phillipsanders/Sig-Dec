# Destructive actions confirm first

- **Date:** 2026-09-14
- **Decision:** DEC-0004
- **Decided by:** product, legal

In the context of **actions that remove data or move money in shared accounts**, facing harm that falls on
the account holder who did not act, we decided that **every such action confirms first, in a dialog that
names the consequence**, and neglected an immediate action with an undo message, to protect the person who
is not in the room, accepting one extra tap for the person who is.

**Ruled out.** An undo message: a joint holder who is not looking at the screen cannot undo anything.
A confirmation only above an amount threshold: the threshold would differ by market and be argued forever.

**Open.** Whether archiving, which can be reversed, counts as removing data. See `decisions/calls/`.
