# Icon-only buttons have an accessible name

- **Date:** 2026-09-20
- **Decision:** DEC-0042
- **Decided by:** accessibility

In the context of **buttons that show an icon and no label**, facing screen readers that announce only
"button", we decided that **every icon-only button has an accessible name set in the component API**, and
neglected relying on the icon or a tooltip, to meet WCAG 2.2 success criterion 4.1.2 (level A), accepting a
required property that has no visual rendering.
