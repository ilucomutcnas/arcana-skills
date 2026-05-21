# Creative QA Gate Automation

## Purpose
Guide pre-handoff review and decision systems: QA checklist automation, validation matrices, stakeholder signoff, revision loops, release blockers, and evidence packs.

## When to Use
Use before any release candidate is packaged by `creative-asset-handoff`, especially for cross-channel campaigns spanning ad copy, editorial content, vector, raster, and PDF deliverables.

## Required Inputs
- Approved brief with channel goals and success constraints.
- Deliverable matrix with owners, versions, and deadlines.
- Current outputs from `ad-creative`, `content-creator`, `vector-workflow-automation`, `raster-retouch-pipeline`, and `pdf-processing` where applicable.
- Compliance requirements (brand, legal, platform, accessibility, licensing/security).

## QA Taxonomy
1. Spec compliance.
2. Brand compliance.
3. Channel/platform compliance.
4. File/export correctness.
5. Accessibility/readability.
6. Legal and disclaimer integrity.
7. Provenance/licensing/security notes.
8. Performance/ad variation readiness.
9. Stakeholder approval state.

## Automated vs Manual Checks
- Automated: character limits, naming/version patterns, SVG viewBox/stroke checks, PDF field/page metadata checks, dimension/size checks.
- Manual: claim substantiation, tone fit, visual realism, legal nuance, strategic acceptability.

## Severity and Release Blockers
- Blocker: legal/compliance failure, missing ownership/signoff, wrong channel specs, missing provenance, corrupted exports.
- Major: inconsistent tone, non-blocking format mismatches, incomplete evidence.
- Minor: wording polish, optional optimization ideas.

## Revision Loop Protocol
1. Log issue with taxonomy + severity + owner + due date.
2. Route to owning mini-skill.
3. Re-run affected checks only, then final regression gate.
4. Capture pass evidence and update signoff state.

## Signoff Matrix
Minimum approvers: creative lead, channel owner, compliance/legal reviewer (if claims), operations/release owner.

## Evidence Pack
Include check matrix, issue log, resolved blockers, signoff matrix, final file manifest hash/list, and go/no-go rationale.

## Failure Modes and Rejection Criteria
Reject release when blockers remain open, evidence is missing, signoff is partial, or platform acceptance gates are not met.
