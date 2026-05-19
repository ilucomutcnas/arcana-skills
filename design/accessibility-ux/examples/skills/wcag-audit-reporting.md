# Example: Subscription Checkout Accessibility Audit Report

## Executive Scope
Audit scope covered account creation, payment modal, coupon workflow, and confirmation route across desktop and mobile. Out of scope: native app checkout.

## Severity Table
| Issue ID | Finding | Severity | User impact | Owner |
|---|---|---|---|---|
| AX-101 | Payment modal loses focus on validation error | Critical | Keyboard and AT users cannot recover quickly | Checkout FE |
| AX-113 | Status message not announced after coupon apply | High | Users miss pricing state change | Commerce FE |
| AX-127 | Low contrast helper text in dark mode | Medium | Reduced readability at night mode | Design Systems |

## WCAG Mapping
| Issue ID | WCAG Criterion | Level | Evidence |
|---|---|---|---|
| AX-101 | 2.4.3 Focus Order / 3.3.1 Error Identification | A | keyboard path + DOM snippet |
| AX-113 | 4.1.3 Status Messages | AA | NVDA + VoiceOver notes |
| AX-127 | 1.4.3 Contrast (Minimum) | AA | contrast sample records |

## Remediation Backlog
- AX-101: Add error summary anchor and focus restoration; due 2026-05-29; dependency: modal utility patch.
- AX-113: Add polite live region update with deduping; due 2026-05-30.
- AX-127: Update token pair to meet 4.5:1; due 2026-05-27.

## Evidence Pack Summary
Evidence pack includes route IDs, keyboard paths, code excerpts, SR transcript notes, and browser/AT matrix runs for NVDA+Firefox and VoiceOver+Safari.

## Retest Plan and Stakeholder Summary
Retest on staging after merge with reruns of checkout critical path. Release approval requires all critical/high findings closed and medium issues tracked with owner/date.
