# governance Reference

## When to Use
Use this skill when governance decisions affect cross-team system consistency and release safety.

## Required Inputs
- Product scope, platform constraints, accessibility requirements
- Existing tokens/components/themes and changelog history
- Owner list, review gates, and rollout milestones

## Workflow
1. Define target outcomes and non-goals.
2. Apply decision rules and constraints for governance.
3. Produce implementation artifacts and review checklist.
4. Validate against failure modes and handoff expectations.

## Decision Rules
- Prefer semantic intent over local shortcuts.
- Keep backward compatibility unless breaking change is approved.
- Require measurable acceptance criteria before release.

## Checklist
- Scope and dependencies documented
- Accessibility and test evidence attached
- Migration impact and rollback path defined
- Ownership and sign-off recorded

## Anti-Patterns
- One-off overrides bypassing system contracts
- Missing version/deprecation notes
- Ambiguous ownership or no release gate

## Handoff Expectations
- Designers provide annotated specs and intent notes.
- Engineers provide mapping, tests, and rollout plan.
- PM/enablement owners provide adoption communication and KPI target.

## Failure Modes
- Contract drift between design files and code tokens/components.
- Release notes that omit migration steps for downstream teams.
- Incomplete test matrix across states, themes, and platforms.

## Escalation Triggers
Escalate to governance and review-audit when changes touch multiple products, introduce breaking behavior, or lack measurable rollback conditions.
