# framework-mapping Example

## Scenario: Map semantic tokens across implementation stacks

## Token-to-Code Mapping Table
| Semantic token | Plain CSS/SCSS | CSS Modules | Tailwind | CSS-in-JS |
|---|---|---|---|---|
| `color.action.primary` | `var(--color-action-primary)` | `styles.primary` uses CSS var | `bg-action-primary` utility | `theme.colors.action.primary` |
| `space.3` | `var(--space-3)` | `.stack { gap: var(--space-3) }` | `gap-3` mapped to token | `theme.space[3]` |
| `radius.md` | `var(--radius-md)` | `.card { border-radius: var(--radius-md) }` | `rounded-md` mapped alias | `theme.radii.md` |

## Implementation Notes
- Plain CSS/SCSS: define root CSS variables from token build output.
- CSS Modules: compose semantic utility classes; avoid local hex literals.
- Tailwind: map token contracts in `theme.extend` rather than default palette names.
- CSS-in-JS: reference semantic theme object keys, not primitives.

## Validation Question
Can every mapped component be switched between light/dark and Brand A/B without editing component source code?
