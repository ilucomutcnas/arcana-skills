# Example: Checkout accessibility audit report

## Severity table
| ID | Issue | Severity | User impact |
|---|---|---|---|
| A11Y-021 | Checkout modal traps virtual cursor | Critical | Task completion blocked |
| A11Y-034 | Error summary not announced | High | Validation failures missed |

## WCAG mapping
| ID | Criterion | Level | Notes |
|---|---|---|---|
| A11Y-021 | 2.1.2 No Keyboard Trap | A | Escape/focus return fails |
| A11Y-034 | 4.1.3 Status Messages | AA | Live region silent |

## Remediation backlog
- FE Platform: modal focus recovery patch, due 2026-05-28.
- Checkout Team: error summary live region patch, due 2026-05-30.

## Evidence pack summary
- Keyboard path: `Tab → Submit → Shift+Tab → Escape`.
- SR notes: NVDA/Firefox silent on summary; VoiceOver/Safari partially announces.
- DOM snippets linked per issue.

## Retest and stakeholder summary
Retest on staging with NVDA/Firefox and VoiceOver/Safari; release gate requires both issues pass and no regression in focus ring contrast.
