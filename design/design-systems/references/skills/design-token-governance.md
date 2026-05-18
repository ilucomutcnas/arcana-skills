# design-token-governance Reference

## When to Use
Use when design tokens change across products, themes, or platforms and require lifecycle governance.

## Required Inputs
- Token taxonomy (primitive, semantic, component-level)
- Current token contract and consumers
- Impact matrix by product/framework
- Ownership model and token review board roster

## Semantic Contract Rules
- Primitive tokens express raw values only.
- Semantic tokens map intent and remain stable for consumers.
- Component aliases may change only through governed releases.

## Proposal Workflow
1. Submit token change request with rationale and blast radius.
2. Classify change (patch/minor/major/breaking).
3. Run review board gate with design + engineering + accessibility.
4. Approve migration and release plan before merge.

## Change Classification
- Patch: non-contractual fixes, no consumer changes.
- Minor: additive semantic tokens, backward compatible.
- Major: behavior shifts requiring migration.
- Breaking: removals/renames requiring coordinated rollout.

## Compatibility and CI Validation
- Contract diff check for renamed/removed tokens.
- Lint for naming, scale, and semantic hierarchy.
- Snapshot tests for theme parity and contrast.
- Build fails when migration notes are missing for major/breaking changes.

## Deprecation and Migration Policy
- Mark deprecated tokens with sunset version and replacement token.
- Keep compatibility aliases for one major cycle.
- Provide codemod or mapping table when aliases are infeasible.

## Token Release Checklist
- Decision record approved
- Migration guide and release notes prepared
- QA evidence from representative products
- Rollback plan with trigger metrics

## Failure Modes and Rejection Criteria
Reject if ownership is unclear, semantic contract is undefined, compatibility tests are missing, migration plan is absent, or breaking changes are undocumented.
