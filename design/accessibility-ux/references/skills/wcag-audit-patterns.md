---
name: "wcag-audit-patterns"
title: "WCAG Compliance Guide"
description: "Use for auditing web content against WCAG 2.2 guidelines across all four POUR principles with automated tooling, manual checks, and actionable remediation strategies."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/wcag-audit-patterns.md`
- Examples: `examples/skills/wcag-audit-patterns.md`
- Implementation playbook: `wcag-audit-patterns__resources/implementation-playbook.md`

## Linked Package Files

- Adjacent: `references/skills/fixing-accessibility.md` — for applying targeted fixes
- Adjacent: `references/skills/screen-reader-testing.md` — for manual assistive technology testing
- Validation: `references/skills/ui-visual-validator.md` — for visual compliance checks

## Purpose

Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies. Covers all four POUR principles, conformance levels (A, AA, AAA), automated testing tools, manual audit checklists, and code-level remediation patterns.

For detailed checklists, code patterns, and audit templates, see `wcag-audit-patterns__resources/implementation-playbook.md`.

## When to Use

- When conducting accessibility audits
- When fixing WCAG violations
- When implementing accessible components from scratch
- When preparing for accessibility lawsuits or compliance reviews
- When meeting ADA, Section 508, or EN 301 549 requirements
- When achieving VPAT compliance

## Workflow

1. Run automated scans (axe-core, Lighthouse, WAVE) to collect initial findings.
2. Perform manual checks: keyboard navigation, focus order, screen reader flows.
3. Map each issue to a WCAG criterion, severity level, and remediation guidance.
4. Apply fixes, prioritizing critical blockers first.
5. Re-test after fixes and document residual risk and compliance status.

## Quality Standards

- Audit against WCAG 2.2 Level AA as minimum standard.
- Automated tools catch 30-50% of issues — always supplement with manual testing.
- Map every finding to a specific WCAG success criterion.
- Classify violations by impact: Critical (blockers), Serious, Moderate, Minor.
- Provide actionable, code-level remediation for each violation.

## Technical Rules

WCAG conformance levels: A (minimum), AA (standard/regulatory), AAA (enhanced).

POUR principles:
- Perceivable: text alternatives, captions, adaptable content, distinguishable presentation.
- Operable: keyboard access, enough time, no seizure triggers, navigable structure.
- Understandable: readable text, predictable behavior, input assistance.
- Robust: compatible with assistive technology, correct ARIA usage.

Common critical violations: missing alt text for functional images, no keyboard access to interactive elements, missing form labels, auto-playing media without controls.

Automated tools: axe-core, Lighthouse, WAVE, pa11y.

## Validation

- Verify all automated findings addressed or documented as accepted risk.
- Confirm manual checks cover keyboard, screen reader, and visual inspection.
- Validate fixes do not introduce new violations.
- Document conformance status per WCAG criterion.

## Restrictions

- Does not provide legal advice or formal certification.
- Automated scans alone are not sufficient — manual verification required.
- Access to UI or source code needed for remediation.

## Output Requirements

- Audit report mapping findings to WCAG criteria with severity.
- Code-level remediation recommendations.
- Residual risk documentation for unresolved issues.
- Re-test confirmation after fixes.
