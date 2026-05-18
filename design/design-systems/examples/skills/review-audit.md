# review-audit Example

## Scenario: Audit of product-library divergence in dark mode

Observed issues in product app:
- Hardcoded text color `#666666` on `#1F2937` cards
- Custom button class overrides `background: #0055FF` bypassing tokens
- Dark-mode overrides force `#FFFFFF` borders causing glare

## Severity Table
| Finding | Type | Severity | Reason |
|---|---|---|---|
| Hardcoded `#666666` text | Product misuse | High | Contrast failure in dark mode |
| Custom button override | System gap + misuse | High | Missing variant plus unauthorized override |
| White borders in dark mode | Product misuse | Medium | Theme token contract bypassed |

## System Gap vs Product Misuse
- System gap: missing tokenized quiet-button variant caused teams to improvise.
- Product misuse: teams bypassed semantic token contract instead of requesting variant.

## Remediation Backlog
1. Add quiet-button semantic variant in system (`P1`, owner: component team).
2. Replace hardcoded colors with `color.text.secondary` token in audited products (`P1`, owner: product squads).
3. Add lint rule blocking raw hex in component-layer CSS (`P2`, owner: platform).
4. Re-audit after two sprints; success if zero high-severity issues remain.
