# library-architecture Example

## Scenario
A maintainer executes an end-to-end **library-architecture** workflow for a Pretext change candidate and prepares review evidence.

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

## Change Request
Add `lineOverflowHint` metadata emitted by `layout` and consumed by diagnostics pages.

## API Impact Table
| Surface | Impact | Compatibility |
|---|---|---|
| layout output | new optional field | backward compatible |
| analyze summary | reads new field if present | backward compatible |

## Responsibility Map
- prepare: no semantic change
- layout: compute hint from break decisions
- analyze: aggregate hint counts for reports
