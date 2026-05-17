# Self-Diagnostic Protocol

## Purpose
Run a proportional integrity check before using this package so routing and outputs remain reliable.

## Tier 1: Quick Integrity Check
Verify package control files exist and are readable:
- `SKILL.md`
- `composition-protocol.md`
- `resources/manifest.json`
- `resources/skill-catalog.md`
- `resources/routing-guide.md`
- `resources/asset-link-index.md`

## Tier 2: Activated Scope Check
For selected mini-skills, verify:
- reference and example paths exist,
- manifest slugs match catalog and routing guide,
- linked assets exist if declared.

## Quality Checks for Stage 3 Creative Coverage
Reject working outputs when any condition is true:
- destructive edits were applied in raster workflows (flattened masters or overwritten originals),
- source/export separation is unclear or mixed,
- provenance/licensing notes are missing for delivered assets,
- export formats are mismatched to channel constraints,
- acceptance criteria are missing or not auditable,
- vector files violate viewport/naming/token hygiene requirements.

## Tier 3: Full Package Audit
Use only when task scope is package quality, migration, or broad repair.

## Severity
- Critical: routing breakage, missing primary references, or unusable active mini-skills.
- Major: inconsistent manifest/catalog/routing mappings or missing adjacent files.
- Minor: non-blocking clarity issues.
