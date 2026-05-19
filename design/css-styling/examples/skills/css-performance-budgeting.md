# css-performance-budgeting Example

## Scenario
Checkout and marketing pages regress after adding new utility bundles and hero effects.

## Before/After Budget Table
| Metric | Budget | Before | After (regressed) | After (fixed) |
|---|---:|---:|---:|---:|
| Route CSS (gzip) | <= 90KB | 78KB | 112KB | 84KB |
| Unused CSS | <= 20% | 18% | 41% | 16% |
| Style Recalc (p75) | <= 45ms | 34ms | 77ms | 39ms |
| Layout events/frame | <= 3 | 2 | 7 | 2 |
| Dropped frames | <= 2% | 1.1% | 9.4% | 1.8% |

## Suspected Causes
- Deep descendant selectors in promo module.
- Duplicated theme utilities across breakpoints.
- `box-shadow` + `filter` animation on hero cards.

## Diagnostic Plan
- Capture Chrome performance traces on mobile emulation.
- Compare Safari and Firefox for selector matching differences.
- Run coverage tooling to identify unused route CSS.

## Remediation Plan
1. Replace deep selectors with component-scoped classes.
2. Consolidate theme utilities into semantic tokens.
3. Move hero animation to transform/opacity and trim shadows.
4. Split non-critical promo styles from critical CSS path.

## Acceptance Criteria
- All metrics return within budget table targets.
- No new high-severity findings in css-review-audit.
- Reduced-motion mode has equivalent UX without heavy effects.

## Handoff Notes
Frontend owner publishes trace links and budget dashboard delta.
Design owner signs off visual parity for hero, checkout summary, and CTA sections.
