# Structural Issues Audit (Issue #4)

> Scope: audit/classification only. No package files were modified in this task.

## Inputs

- `docs/audits/REPOSITORY_STRUCTURE_MAP.json` (primary)

## Summary

- Total issues: **19**
- Critical: **1**
- High: **10**
- Medium: **2**
- Low: **5**
- Info: **1**
- Affected packages: **8**

## Issue List

### STRUCT-001 — Missing shared-rules/ compared with peer packages
- Severity: `low`
- Category: `required-structure`
- Package: `design/3d-animation`
- Path: `design/3d-animation/shared-rules/`
- Evidence: Domain design has 4/8 packages with shared-rules/, but design/3d-animation does not.
- Impact: Reduced cross-skill consistency relative to peers in same domain.
- Recommended follow-up: Assess whether shared-rules/ is needed for this package and add if structurally relevant.

### STRUCT-002 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/3d-animation`
- Path: `design/3d-animation/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-003 — Missing shared-rules/ compared with peer packages
- Severity: `low`
- Category: `required-structure`
- Package: `design/accessibility-ux`
- Path: `design/accessibility-ux/shared-rules/`
- Evidence: Domain design has 4/8 packages with shared-rules/, but design/accessibility-ux does not.
- Impact: Reduced cross-skill consistency relative to peers in same domain.
- Recommended follow-up: Assess whether shared-rules/ is needed for this package and add if structurally relevant.

### STRUCT-004 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/accessibility-ux`
- Path: `design/accessibility-ux/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-005 — Missing shared-rules/ compared with peer packages
- Severity: `low`
- Category: `required-structure`
- Package: `design/brand-visual`
- Path: `design/brand-visual/shared-rules/`
- Evidence: Domain design has 4/8 packages with shared-rules/, but design/brand-visual does not.
- Impact: Reduced cross-skill consistency relative to peers in same domain.
- Recommended follow-up: Assess whether shared-rules/ is needed for this package and add if structurally relevant.

### STRUCT-006 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/brand-visual`
- Path: `design/brand-visual/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-007 — Binary assets present in package
- Severity: `low`
- Category: `asset-generated`
- Package: `design/brand-visual`
- Path: `design/brand-visual`
- Evidence: counts.binary_asset_files=55 for design/brand-visual.
- Impact: Binary files raise review and maintenance overhead.
- Recommended follow-up: Track provenance and cleanup policy in asset-link-index.

### STRUCT-008 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/content-writing`
- Path: `design/content-writing/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-009 — Missing shared-rules/ compared with peer packages
- Severity: `low`
- Category: `required-structure`
- Package: `design/creative-tools`
- Path: `design/creative-tools/shared-rules/`
- Evidence: Domain design has 4/8 packages with shared-rules/, but design/creative-tools does not.
- Impact: Reduced cross-skill consistency relative to peers in same domain.
- Recommended follow-up: Assess whether shared-rules/ is needed for this package and add if structurally relevant.

### STRUCT-010 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/creative-tools`
- Path: `design/creative-tools/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-011 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/css-styling`
- Path: `design/css-styling/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-012 — Package entry router issue (SKILL.me)
- Severity: `critical`
- Category: `discovery`
- Package: `design/design-systems`
- Path: `design/design-systems/SKILL.me`
- Evidence: core_files.skill_md=False and core_files.skill_me=True for design/design-systems.
- Impact: Skill discovery/routing can fail for the package.
- Recommended follow-up: Add a valid SKILL.md router in a dedicated structural fix issue.

### STRUCT-013 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/design-systems`
- Path: `design/design-systems/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-014 — Manifest records missing required fields (purpose/when)
- Severity: `high`
- Category: `manifest`
- Package: `design/pretext-ui`
- Path: `design/pretext-ui/resources/manifest.json`
- Evidence: One or more manifest records do not include all required fields: title, slug, purpose, when, reference, examples.
- Impact: Manifest integrity is incomplete for downstream tooling and registry generation.
- Recommended follow-up: Add required fields to every manifest record.

### STRUCT-015 — Large files above 500KB present
- Severity: `medium`
- Category: `asset-generated`
- Package: `design/pretext-ui`
- Path: `design/pretext-ui`
- Evidence: counts.large_files=3 for design/pretext-ui.
- Impact: Large generated/data files can bloat repository and complicate maintenance.
- Recommended follow-up: Confirm necessity and document generation/source strategy.

### STRUCT-016 — Missing root registry.json
- Severity: `high`
- Category: `repository-level`
- Package: `_repository`
- Path: `registry.json`
- Evidence: registry.json is absent from repository_files list.
- Impact: No canonical root package registry is available for automated discovery/validation.
- Recommended follow-up: Add root registry.json in dedicated registry issue.

### STRUCT-017 — Missing root registry.schema.json
- Severity: `high`
- Category: `repository-level`
- Package: `_repository`
- Path: `registry.schema.json`
- Evidence: registry.schema.json is absent from repository_files list.
- Impact: Registry validation contract is missing for future automation.
- Recommended follow-up: Add root registry.schema.json in dedicated registry issue.

### STRUCT-018 — Missing root-level registry documentation
- Severity: `medium`
- Category: `repository-level`
- Package: `_repository`
- Path: `README.md`
- Evidence: No root markdown file containing 'registry' appears in repository_files.
- Impact: Contributors lack repository-level guidance for package registry conventions.
- Recommended follow-up: Add root registry documentation describing format and maintenance workflow.

### STRUCT-019 — Domain imbalance against multi-plane repository vision
- Severity: `info`
- Category: `repository-level`
- Package: `_repository`
- Path: `README.md`
- Evidence: Repository map lists one domain with packages: design.
- Impact: Roadmap breadth may be constrained until additional planned domains are introduced.
- Recommended follow-up: Track onboarding of additional domains in future planning issues.
