# accessibility Example

## Scenario: Accessibility audit of account settings form components

## Audit Table
| Check | Result | Evidence | Remediation |
|---|---|---|---|
| Contrast (text/input/help text) | Fail | Label at `#6B7280` on `#FFFFFF` = 4.0:1 | Map label token to `color.text.secondary-strong` |
| Focus order and visibility | Partial | Modal close button receives focus late | Fix DOM order and add initial focus trap |
| Keyboard operability | Fail | Custom toggle not activatable by Space | Add button semantics and key handlers |
| Icon-only labeling | Fail | Save icon button has no accessible name | Add `aria-label="Save settings"` |
| Target sizing | Partial | Small icon actions at 28x28 | Increase to 44x44 touch area |
| Reduced motion | Fail | Success animation ignores reduced-motion | Gate animation duration to 0ms preference path |

## Remediation Plan
1. Patch token mappings for contrast in next patch release.
2. Fix keyboard/focus defects before feature freeze.
3. Add CI check for icon-only controls missing labels.
4. Add reduced-motion regression scenario in Storybook test suite.

## Evidence Checklist
- Axe and keyboard walkthrough recordings
- Screen reader transcript for submit/success flow
- Contrast report for light/dark theme variants
- Signed QA verification for all remediated defects
