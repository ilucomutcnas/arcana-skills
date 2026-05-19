# Self-Diagnostic Protocol

## Quick Integrity Check

Before routing, verify readability of:
- `SKILL.md`
- `composition-protocol.md`
- `resources/skill-catalog.md`
- `resources/routing-guide.md`
- `resources/asset-link-index.md`
- `resources/manifest.json`

## Activated Scope Check

For selected mini-skills verify:
- reference + example file existence;
- links and route slugs consistent across SKILL/catalog/routing/manifest;
- selected evidence can be produced from available scripts/pages/corpora.

## Evidence Gating Checks

- **Public API touched?** Require `library-architecture` impact boundary + compatibility/migration note.
- **Browser accuracy claim?** Require cross-browser evidence (Chromium/Firefox/WebKit or documented constraint).
- **Performance claim?** Require benchmark/profiling evidence, not anecdotal timing.
- **Corpus impact?** Require canary + width/script matrix confirmation.
- **Packaging/release impact?** Require dist/export/smoke checks.
- **Demo impact?** Require dogfooding scenario verification.
- **Research implication?** Require linkage to prior accepted/rejected hypotheses.
- **Escalation needed?** Route to `architecture-review` when risk crosses API, release, or systemic behavior boundaries.

## Rejection Criteria

Reject or block the proposal when any applies:
- Missing browser evidence for accuracy conclusions.
- Performance claims without benchmarks or profiles.
- API changes without compatibility/migration analysis.
- Release claims without package smoke and export checks.
- Roadmap proposals that reopen previously rejected work without new evidence.

## Severity

- **Critical:** missing primary reference/example, broken manifest paths, absent release/API evidence for high-risk changes.
- **Major:** incomplete adjacent evidence, weak mismatch taxonomy, missing demo QA for UI behavior changes.
- **Minor:** formatting/narrative issues that do not affect execution safety.
