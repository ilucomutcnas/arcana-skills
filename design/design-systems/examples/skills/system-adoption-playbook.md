# system-adoption-playbook Example

## Multi-Product Rollout Scenario
Three products (Commerce, Admin, Support) migrate to shared component and token system over two quarters.

## Migration Wave Plan
- Wave 1: Admin (low traffic, high UI variance)
- Wave 2: Support (medium traffic, moderate dependency)
- Wave 3: Commerce (high traffic, strict stability gates)

## Stakeholder Table
- VP Product: sponsor
- Design Systems Manager: program owner
- Frontend Platform Lead: technical owner
- QA Lead: release evidence owner

## Adoption KPI Table
- Component adoption target: 70% Q1, 90% Q2
- Deprecated patterns reduced by 50% each wave
- Accessibility P1 defects: zero at release
- Training completion: >95%

## Exception Register
- Legacy checkout allowed temporary exception until Wave 3 + 1 sprint
- Expiry date and owner documented; mitigation tracked weekly

## Communication Plan
- Biweekly migration digest
- Weekly office hours
- Release readiness checkpoints per wave

## Acceptance Criteria
- Each wave meets KPI targets and quality gates
- No undocumented exceptions
- Post-wave retrospective actions assigned and tracked
