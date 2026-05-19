# Example: Checkout + Filter Modal Edge-Case Investigation

## Scenario
Users reported intermittent checkout failures when applying filters in a side modal before proceeding to payment on mobile and desktop.

## AT/Input Matrix
| Flow | Environment | Result |
|---|---|---|
| Apply filter then close modal | Voice Control + iOS Safari | Command "Tap Apply" misses unlabeled icon button |
| Move through modal actions | Switch Control + iPadOS | Focus loop skips confirmation action |
| Review summary panel | NVDA + Firefox at 400% zoom | Focus jumps outside viewport |
| Confirm cart totals | Windows Forced Colors + Edge | Active row highlight disappears |

## Failure Taxonomy and Plan
Failures mapped to naming, focus recovery, zoom reflow, and forced-colors token issues. Remediation plan assigned to design systems and checkout FE with due dates and criterion mapping.

## Retest Checklist and Acceptance
Retest includes command targeting, sequential focus, zoom persistence, forced-colors visibility, and live region cadence. Acceptance requires zero blocking failures and clear owners for any residual medium issues.
