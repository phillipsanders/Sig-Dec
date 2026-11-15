# danger-colour-use

- **Decision:** DEC-0043 (promoted; the check stays to catch regressions)
- **Reads:** the Figma file under test (read-only), and `tokens/harbor.tokens.json`

## Steps

1. List every layer whose fill or stroke is bound to `color.feedback.danger`.
2. Pass if the layer belongs to a destructive action, an error message or an error state.
3. Fail if it is used for emphasis, marketing or decoration.
4. Also fail any destructive action that binds `color.brand.primary`.

## Report

One line per failing layer: frame, layer, bound token.
