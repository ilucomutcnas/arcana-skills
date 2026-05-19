# browser-accuracy Example

## Scenario
A maintainer executes an end-to-end **browser-accuracy** workflow for a Pretext change candidate and prepares review evidence.

## Stages
1. Define task, constraints, and impacted modules/pages/scripts.
2. Run relevant commands and collect structured evidence tables.
3. Apply fix/update and re-run checks.
4. Summarize decision, residual risk, and acceptance criteria.

## Evidence Capture Table
| Area | Before | After | Decision |
|---|---|---|---|
| Behavior/metric | baseline observed | candidate observed | accept/block |

## Acceptance Criteria
- Evidence is reproducible by another contributor.
- Decision includes fix/accept/refresh rationale where applicable.
- Handoff notes include follow-up actions and ownership.

## Example additions
Scenario: Chromium and Firefox wrap differently at 640px while WebKit matches Firefox.
Mismatch table includes browser, symptom, severity, suspected layer, decision.
Final decision chosen after diagnosis: fix engine contract or refresh snapshot with rationale.
