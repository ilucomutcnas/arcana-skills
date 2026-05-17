# Manifest and Routing Consistency Audit

This report is audit-only. No package remediation or package-content edits were performed in this issue.

## Scope

Audit coverage included manifest, catalog, routing, reference, example, asset-link index, shared-rules (if present), SKILL router, composition protocol, and self-diagnostic protocol files across all detected packages.

## Summary

| Metric | Value |
|---|---:|
| package_count | 8 |
| total_findings | 8 |
| critical | 0 |
| high | 0 |
| medium | 4 |
| low | 4 |
| info | 0 |
| packages_with_findings | 4 |

## Package Overview

| Package | Manifest Records | References | Examples | Catalog | Routing Guide | Asset Index | Shared Rules | Findings | Highest Severity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| design/3d-animation | 16 | 16 | 16 | True | True | True | True | 2 | medium |
| design/accessibility-ux | 6 | 6 | 6 | True | True | True | True | 2 | medium |
| design/brand-visual | 9 | 9 | 9 | True | True | True | True | 2 | medium |
| design/content-writing | 8 | 8 | 8 | True | True | True | True | 0 | none |
| design/creative-tools | 3 | 3 | 3 | True | True | True | True | 2 | medium |
| design/css-styling | 12 | 12 | 12 | True | True | True | True | 0 | none |
| design/design-systems | 8 | 8 | 8 | True | True | True | True | 0 | none |
| design/pretext-ui | 10 | 10 | 10 | True | True | True | True | 0 | none |

## Critical

No findings.

## High

No findings.

## Medium

### MRC-001 - Shared rules are not referenced in router or routing guide
- severity: `medium`
- category: `shared-rules-routing`
- package: `design/3d-animation`
- path: `design/3d-animation/SKILL.md`
- evidence: Package contains shared-rules/, but neither SKILL.md nor resources/routing-guide.md references shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Cross-skill routing guidance can miss shared constraints during mini-skill selection.
- recommended follow-up: Update SKILL.md and/or resources/routing-guide.md to reference shared-rules usage in a dedicated remediation issue.

### MRC-003 - Shared rules are not referenced in router or routing guide
- severity: `medium`
- category: `shared-rules-routing`
- package: `design/accessibility-ux`
- path: `design/accessibility-ux/SKILL.md`
- evidence: Package contains shared-rules/, but neither SKILL.md nor resources/routing-guide.md references shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Cross-skill routing guidance can miss shared constraints during mini-skill selection.
- recommended follow-up: Update SKILL.md and/or resources/routing-guide.md to reference shared-rules usage in a dedicated remediation issue.

### MRC-005 - Shared rules are not referenced in router or routing guide
- severity: `medium`
- category: `shared-rules-routing`
- package: `design/brand-visual`
- path: `design/brand-visual/SKILL.md`
- evidence: Package contains shared-rules/, but neither SKILL.md nor resources/routing-guide.md references shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Cross-skill routing guidance can miss shared constraints during mini-skill selection.
- recommended follow-up: Update SKILL.md and/or resources/routing-guide.md to reference shared-rules usage in a dedicated remediation issue.

### MRC-007 - Shared rules are not referenced in router or routing guide
- severity: `medium`
- category: `shared-rules-routing`
- package: `design/creative-tools`
- path: `design/creative-tools/SKILL.md`
- evidence: Package contains shared-rules/, but neither SKILL.md nor resources/routing-guide.md references shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Cross-skill routing guidance can miss shared constraints during mini-skill selection.
- recommended follow-up: Update SKILL.md and/or resources/routing-guide.md to reference shared-rules usage in a dedicated remediation issue.


## Low

### MRC-002 - Asset-link index omits shared-rules references
- severity: `low`
- category: `asset-index`
- package: `design/3d-animation`
- path: `design/3d-animation/resources/asset-link-index.md`
- evidence: Package contains shared-rules/, but resources/asset-link-index.md does not mention shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Auxiliary index documentation is incomplete for package support files.
- recommended follow-up: Document shared-rules artifacts in resources/asset-link-index.md during remediation.

### MRC-004 - Asset-link index omits shared-rules references
- severity: `low`
- category: `asset-index`
- package: `design/accessibility-ux`
- path: `design/accessibility-ux/resources/asset-link-index.md`
- evidence: Package contains shared-rules/, but resources/asset-link-index.md does not mention shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Auxiliary index documentation is incomplete for package support files.
- recommended follow-up: Document shared-rules artifacts in resources/asset-link-index.md during remediation.

### MRC-006 - Asset-link index omits shared-rules references
- severity: `low`
- category: `asset-index`
- package: `design/brand-visual`
- path: `design/brand-visual/resources/asset-link-index.md`
- evidence: Package contains shared-rules/, but resources/asset-link-index.md does not mention shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Auxiliary index documentation is incomplete for package support files.
- recommended follow-up: Document shared-rules artifacts in resources/asset-link-index.md during remediation.

### MRC-008 - Asset-link index omits shared-rules references
- severity: `low`
- category: `asset-index`
- package: `design/creative-tools`
- path: `design/creative-tools/resources/asset-link-index.md`
- evidence: Package contains shared-rules/, but resources/asset-link-index.md does not mention shared-rules, STYLE-GUARDRAILS.md, or ANTI-PATTERNS.md.
- impact: Auxiliary index documentation is incomplete for package support files.
- recommended follow-up: Document shared-rules artifacts in resources/asset-link-index.md during remediation.


## Info

No findings.
## Recommended Follow-up Order

1. Address critical findings first (none in this audit if empty).
2. Resolve high-severity manifest link/sync issues blocking reliable mini-skill routing.
3. Correct medium router/routing/shared-rules consistency issues.
4. Resolve low documentation alignment issues and standardization info notes.
