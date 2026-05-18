# theming Example

## Scenario: Add second brand plus dark mode

A platform supports Brand A and Brand B. Both require light/dark themes and high-contrast safe actions.

## Semantic Theme Mapping Table
| Semantic token | Brand A Light | Brand A Dark | Brand B Light | Brand B Dark |
|---|---|---|---|---|
| `color.bg.canvas` | `#FFFFFF` | `#0F172A` | `#FFFBF5` | `#1A120B` |
| `color.text.primary` | `#111827` | `#F8FAFC` | `#2B2118` | `#FDF6EC` |
| `color.action.primary` | `#1D4ED8` | `#60A5FA` | `#B45309` | `#F59E0B` |

## Fallback Rules
1. If brand-specific semantic token is missing, fall back to global semantic token.
2. If dark-mode token is missing, use light token only for non-text decorative surfaces.
3. Never fall back from semantic token to raw primitive in product code.

## Rollout and Regression QA Plan
- Snapshot matrix: 10 core components × 4 theme modes
- Contrast tests for text/action/focus tokens in all theme pairs
- Visual diff threshold: max 0.5% changed pixels outside approved areas
- Pilot release to internal admin before public commerce rollout
