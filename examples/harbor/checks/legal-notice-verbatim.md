# legal-notice-verbatim

- **Decision:** DEC-0041
- **Reads:** the Figma file of the flow under test (read-only), and `history/legal-notices.md`

## Steps

1. For each notice in `history/legal-notices.md`, find the frames of its flow.
2. Collect the text layers on the frame that comes before the action the notice concerns.
3. Pass if the notice appears word for word, ignoring line breaks and repeated spaces.
4. Fail if it is shortened, reworded, placed in a tooltip or replaced by a link.

## Report

One line per notice: flow, frame, pass or fail, and the first words that differ.
