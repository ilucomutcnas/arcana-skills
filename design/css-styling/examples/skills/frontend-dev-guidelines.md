# frontend-dev-guidelines Example

## Scenario
Realistic product delivery workflow for `frontend-dev-guidelines` with end-to-end QA.

## Implementation Highlights
- Defined scope, states, and component/page matrix.
- Applied token and cascade constraints.
- Added accessibility checks (focus, contrast, keyboard, reduced-motion when applicable).
- Added responsive checks with explicit width-state table or breakpoint evidence.
- Added regression gate criteria before merge.

## Acceptance Criteria
- No severity-1 styling regressions.
- Cross-browser checks complete (Chrome/Safari/Firefox).
- Performance impact documented with rationale.
- Handoff includes implementation notes for design + frontend reviewers.

## QA Gates
- Width/device checks completed and documented.
- Accessibility and interaction states validated with evidence.
- Reviewer checklist includes rollback plan if regressions appear after merge.
