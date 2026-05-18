# governance Example

## Scenario: Governance model for quarterly design-system releases

## Governance Areas
- Token changes
- Component API changes
- Accessibility compliance
- Documentation quality
- Deprecation and migration readiness

## Review Gate Questions
- Is this change backward compatible?
- Are migration notes explicit for consumers?
- Is ownership assigned for rollout and support?
- Are accessibility/test artifacts attached?

## Versioning Model
- Patch: non-breaking defect fixes
- Minor: additive features with compatibility
- Major: breaking changes with migration plan

## RFC Workflow
1. Author RFC with scope, risks, and alternatives.
2. Review board (design lead, platform lead, accessibility lead) approves/rejects.
3. Implementation PR includes checklist and release notes.
4. Post-release review tracks adoption and incident metrics.

## Decision Record
- Decision: Deprecate `CardHeaderLegacy` in v5 major cycle.
- Reason: Inconsistent slots and inaccessible heading structure.
- Outcome: New `CardHeader` contract with migration map.

## Deprecation Plan
- Mark legacy component as deprecated in docs and lint warnings.
- Keep compatibility wrapper for one major version.
- Remove after adoption reaches 95% and exceptions are closed.
