# Package Quality Rubric

## Purpose and Scope
This rubric defines Stage 3 package quality evaluation criteria for Arcana Skills packages after Stage 2 structural remediation. It is audit-only: scores and recommendations identify quality maturity and upgrade priorities without editing package content.

Scope:
- Applies to current packages in the `design/` domain listed in the Stage 3 issue.
- Evaluates package quality and readiness, not structural existence only.
- Uses direct repository evidence from manifests, routing/protocol docs, references, examples, and asset index files.

## Maturity Definitions
- **professional**: High quality across most dimensions; package is substantial and dependable for real user work.
- **working**: Coherent and usable, but needs focused upgrades (depth, examples, coverage, or cleanup) before professional classification.
- **amateur**: Too thin, generic, or incomplete for reliable production-level use.

## Status Definitions
- **ready-for-use**: Good enough to use now before Stage 5 registry work.
- **needs-upgrade**: Targeted package improvements needed.
- **needs-major-upgrade**: Substantial expansion or rewrite needed.
- **needs-asset-hygiene**: Content may be usable, but asset/binary hygiene follow-up is required.
- **needs-registry-only**: Package quality is strong; remaining work is mainly Stage 5 registry/schema.

## Scoring Dimensions (0-5 each)
1. `structure_completeness`
2. `manifest_integrity`
3. `routing_clarity`
4. `reference_depth`
5. `example_quality`
6. `domain_coverage`
7. `specificity_and_non_genericness`
8. `professional_readiness`
9. `english_only_readiness`
10. `asset_hygiene_readiness`

## Scoring Scale (per dimension)
- **0**: Missing/unusable.
- **1**: Very weak, mostly placeholder.
- **2**: Partial and limited.
- **3**: Adequate baseline quality.
- **4**: Strong quality with minor gaps.
- **5**: Excellent and production-ready depth.

## Overall Score Interpretation (0-100)
- **90-100**: Typically `professional`; usually `ready-for-use` or `needs-registry-only`.
- **70-89**: Typically `working`; usually `needs-upgrade`.
- **40-69**: `working` or `amateur` based on evidence; often `needs-major-upgrade`.
- **0-39**: `amateur`; `needs-major-upgrade`.

## Evidence Rules
- Use direct file evidence only (package files, manifests, protocol docs, references/examples, Stage 2 status, validator output).
- Every package rating must include specific evidence paths.
- Claims must be audit-observable (no assumptions about external workflows).
- Asset hygiene findings are readiness assessments only; do not make legal conclusions.

## What This Rubric Must Not Do
- Must not modify package content.
- Must not change manifests, registry files, scripts, or binary assets.
- Must not perform remediation, only evaluation.
- Must not inflate maturity from structural completeness alone.

## How Future Upgrade Tasks Should Use This Rubric
- Start with packages in recommended upgrade order from the matrix.
- Convert each `quality_gap` and `recommended_upgrade_action` into scoped remediation issues.
- Re-run validator and package audit checks after upgrades.
- Re-score changed packages using the same 10 dimensions to measure improvement between stages.
