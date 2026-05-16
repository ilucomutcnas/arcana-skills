# Structural Issues Audit

This document is an audit/classification output only; no fixes were implemented and no package files were changed.

## Input Source
- `docs/audits/REPOSITORY_STRUCTURE_MAP.json` (primary source).

## Severity Summary
| Metric | Count |
|---|---:|
| Total issues | 11 |
| critical | 1 |
| high | 2 |
| medium | 2 |
| low | 5 |
| info | 1 |
| affected_package_count | 6 |

## Affected Package Summary
| Package | critical | high | medium | low | info |
|---|---:|---:|---:|---:|---:|
| `design/3d-animation` | 0 | 0 | 0 | 1 | 0 |
| `design/accessibility-ux` | 0 | 0 | 0 | 1 | 0 |
| `design/brand-visual` | 0 | 0 | 0 | 2 | 0 |
| `design/creative-tools` | 0 | 0 | 0 | 1 | 0 |
| `design/design-systems` | 1 | 0 | 0 | 0 | 0 |
| `design/pretext-ui` | 0 | 0 | 1 | 0 | 0 |

## Critical

### STRUCT-006 — Package has SKILL.me instead of SKILL.md
- Category: `discovery`
- Scope: `design/design-systems`
- Path: `design/design-systems/SKILL.me`
- Evidence: Repository map shows skill_md=false and skill_me=true for design/design-systems.
- Impact: Skill discovery may fail because the package does not expose the expected SKILL.md router.
- Recommended follow-up: Rename SKILL.me to SKILL.md in a dedicated structural fix issue.

## High

### STRUCT-008 — Root registry.json is missing
- Category: `repository-level`
- Scope: `_repository`
- Path: `registry.json`
- Evidence: Repository map repository_files does not include registry.json.
- Impact: A canonical root package registry is unavailable for automated discovery and coordination.
- Recommended follow-up: Create registry.json in a dedicated registry issue.

### STRUCT-009 — Root registry.schema.json is missing
- Category: `repository-level`
- Scope: `_repository`
- Path: `registry.schema.json`
- Evidence: Repository map repository_files does not include registry.schema.json.
- Impact: No explicit schema contract exists for validating future root registry data.
- Recommended follow-up: Create registry.schema.json in a dedicated registry issue.

## Medium

### STRUCT-007 — Package contains files larger than 500 KB
- Category: `asset-generated`
- Scope: `design/pretext-ui`
- Path: `design/pretext-ui`
- Evidence: Repository map shows large_files=3 for design/pretext-ui.
- Impact: Large generated/data artifacts can increase repository maintenance overhead.
- Recommended follow-up: Confirm necessity and document generation/source provenance in follow-up issues.

### STRUCT-010 — Root-level package registry documentation is missing
- Category: `repository-level`
- Scope: `_repository`
- Path: `README.md`
- Evidence: Repository map does not list root-level markdown registry documentation.
- Impact: Contributors may lack structural guidance for future registry maintenance.
- Recommended follow-up: Add root-level registry documentation in a dedicated documentation issue.

## Low

### STRUCT-001 — Package is missing shared-rules/ compared to peer packages
- Category: `required-structure`
- Scope: `design/3d-animation`
- Path: `design/3d-animation/shared-rules/`
- Evidence: In domain 'design', 4/8 mapped packages have shared-rules/, while design/3d-animation does not.
- Impact: Cross-skill consistency support may be weaker than comparable packages.
- Recommended follow-up: Assess whether shared-rules/ is structurally relevant for this package and add in a follow-up issue if needed.

### STRUCT-002 — Package is missing shared-rules/ compared to peer packages
- Category: `required-structure`
- Scope: `design/accessibility-ux`
- Path: `design/accessibility-ux/shared-rules/`
- Evidence: In domain 'design', 4/8 mapped packages have shared-rules/, while design/accessibility-ux does not.
- Impact: Cross-skill consistency support may be weaker than comparable packages.
- Recommended follow-up: Assess whether shared-rules/ is structurally relevant for this package and add in a follow-up issue if needed.

### STRUCT-003 — Package is missing shared-rules/ compared to peer packages
- Category: `required-structure`
- Scope: `design/brand-visual`
- Path: `design/brand-visual/shared-rules/`
- Evidence: In domain 'design', 4/8 mapped packages have shared-rules/, while design/brand-visual does not.
- Impact: Cross-skill consistency support may be weaker than comparable packages.
- Recommended follow-up: Assess whether shared-rules/ is structurally relevant for this package and add in a follow-up issue if needed.

### STRUCT-004 — Package contains binary assets
- Category: `asset-generated`
- Scope: `design/brand-visual`
- Path: `design/brand-visual`
- Evidence: Repository map shows binary_asset_files=55 for design/brand-visual.
- Impact: Binary assets are asset-hygiene indicators requiring provenance and maintenance tracking.
- Recommended follow-up: Review and document asset provenance and lifecycle in follow-up issues.

### STRUCT-005 — Package is missing shared-rules/ compared to peer packages
- Category: `required-structure`
- Scope: `design/creative-tools`
- Path: `design/creative-tools/shared-rules/`
- Evidence: In domain 'design', 4/8 mapped packages have shared-rules/, while design/creative-tools does not.
- Impact: Cross-skill consistency support may be weaker than comparable packages.
- Recommended follow-up: Assess whether shared-rules/ is structurally relevant for this package and add in a follow-up issue if needed.

## Info

### STRUCT-011 — Current map shows single-domain coverage
- Category: `repository-level`
- Scope: `_repository`
- Path: `README.md`
- Evidence: Repository map currently lists packages under one domain (design).
- Impact: This is a planning observation for domain expansion, not a blocking defect by itself.
- Recommended follow-up: Track additional domain onboarding in roadmap/follow-up issues.

## Suggested Follow-up Issue Order
1. Resolve `critical` discovery/router issues first (package entry routing).
2. Resolve `high` structural blockers for registry preparation.
3. Resolve `medium` readiness and repository-level documentation gaps.
4. Resolve `low` consistency/hygiene findings (shared-rules parity, binary asset hygiene).
5. Track `info` observations for roadmap sequencing (domain expansion).
