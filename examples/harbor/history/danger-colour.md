# The danger colour is for destructive actions and errors only

- **Date:** 2026-09-14
- **Decision:** DEC-0043 (promoted into the token `color.feedback.danger`)
- **Decided by:** brand, design system

In the context of **two reds that are close in value, the brand red and the danger red**, facing screens
where a sale banner and a delete button looked alike, we decided that **the danger colour is used only for
destructive actions and errors**, and neglected one shared red, so that red on an action always means
"this removes something", accepting two tokens that look similar.

**Promoted.** The rule now lives in the token's description. A component that binds the token for a
destructive action cannot pick the wrong red, so agents no longer receive this decision.
