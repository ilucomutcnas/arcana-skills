---
name: "design-system-review-audit"
title: "Design System Review & Audit"
description: "Audits products or libraries against design-system rules and produces concrete remediation guidance."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/review-audit.md`
- Examples: `examples/skills/review-audit.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Review & Audit

## Purpose
Review interfaces, component libraries, or codebases for system compliance and consistency.

## Audit dimensions
- token compliance
- component reuse
- variant discipline
- accessibility consistency
- theming correctness
- documentation gaps
- divergence and one-off patterns

## Output format
For each issue provide:
1. violation
2. why it matters
3. severity: low / medium / high / critical
4. concrete fix
5. whether this is a local issue or system issue

## Common findings
- raw hardcoded values where semantic tokens should be used
- duplicate components with slightly different names
- dark-mode patches inside feature code
- inconsistent focus styling
- new components created for spacing/layout differences only

## Validation
The audit is complete only when it distinguishes:
- isolated misuse
- gaps in the system itself
- governance failures enabling repeated misuse
