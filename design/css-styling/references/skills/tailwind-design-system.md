# tailwind-design-system

## Operational Scope
Production guidance for tailwind design system with decision rules, constraints, QA evidence, and handoff requirements.

## Workflow
1. Define user flows, states, and page-family scope.
2. Apply architecture constraints (tokens, layers, framework boundaries).
3. Implement with accessibility, responsive, and browser-compat checks.
4. Run diagnostics (DevTools, visual regression, interaction/focus checks).
5. Record regression gates and merge criteria.

## Constraints and Validation
- Include explicit responsive evidence (mobile/tablet/desktop breakpoints or container states).
- Include accessibility checks (focus, contrast, keyboard, reduced motion where relevant).
- Include browser checks for Chrome/Safari/Firefox.
- Reject unmeasured performance claims and undocumented overrides.

## Failure Modes
- Style drift from token system.
- Specificity escalation and brittle overrides.
- State gaps (loading/error/empty/disabled).
- Inconsistent behavior across frameworks or routes.

## Decision Rules
- Define acceptance evidence before edits: screenshots/trace IDs, responsive matrix, and rollback trigger.
- Map constraints to layers/tokens first; avoid ad-hoc local overrides.
- Explicitly document browser differences and fallbacks.

## Diagnostics Playbook
- Use DevTools for computed style and cascade inspection on affected states.
- Record keyboard traversal, focus ring visibility, and contrast at each major state.
- Validate against anti-patterns list and flag severity with owners and due dates.

## Handoff Expectations
- Provide changed selectors/components list and migration notes.
- Include regression gates (blocking vs acceptable) and unresolved risks.
- Link follow-up tickets for deferred improvements with accountable owners.
