---
name: "accessibility-ux"
title: "Accessibility & UX Standards"
description: "Use for WCAG compliance audits, accessibility fixes, screen reader testing, UI visual validation, motion performance optimization, and SEO metadata auditing. Covers ARIA patterns, keyboard navigation, focus management, contrast requirements, assistive technology compatibility, and inclusive design practices."
version: "1.0.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide structured guidance for building, auditing, and fixing accessible web interfaces. This domain covers WCAG 2.2 compliance, practical accessibility fixes, screen reader testing, visual validation, animation performance, and page metadata correctness — the full scope of making web UIs perceivable, operable, understandable, and robust.

## Domain Coverage

This package represents the accessibility and UX standards domain. It covers multiple interconnected capabilities: fixing specific accessibility violations, auditing against WCAG criteria, testing with screen readers, validating visual output, optimizing motion performance, and ensuring correct page metadata.

Mini-skills are separated for routing and selective loading. Real accessibility work rarely depends on one skill alone — a WCAG audit typically requires combining compliance knowledge with screen reader testing and targeted fixes.

## How to Use

1. Always begin with self-diagnostic. Start with a quick package integrity check, then validate only the activated working set. The self-diagnostic rules are defined in `self-diagnostic-protocol.md`.
2. Identify the primary mini-skill that best matches the task.
3. Check the Multi-Skill Activation Guide below to load adjacent mini-skills that commonly co-occur with the primary task.
4. Open the corresponding reference file under `references/skills/`.
5. Open the corresponding examples file under `examples/skills/` if concrete code is needed.
6. Use `resources/skill-catalog.md` for the full index.
7. Use `resources/routing-guide.md` when a task spans multiple mini-skills.
8. Use `resources/asset-link-index.md` to find every auxiliary folder and file.

## Multi-Skill Activation Guide

Do not treat mini-skills as isolated when the task spans multiple concerns. For all non-trivial tasks, apply the universal composition rule in `composition-protocol.md`.

Common combinations:

- **Full accessibility audit**: wcag-audit-patterns (primary) + fixing-accessibility + screen-reader-testing + ui-visual-validator
- **Fixing UI components**: fixing-accessibility (primary) + wcag-audit-patterns + screen-reader-testing
- **Screen reader compatibility**: screen-reader-testing (primary) + fixing-accessibility + wcag-audit-patterns
- **Visual regression review**: ui-visual-validator (primary) + fixing-accessibility + wcag-audit-patterns
- **Animation performance**: fixing-motion-performance (primary) + fixing-accessibility + ui-visual-validator
- **SEO and metadata**: fixing-metadata (primary) + ui-visual-validator + fixing-accessibility

## Package Structure

- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted code snippets and usage samples

## Mini-Skills Index

### fixing-accessibility
- Summary: Review and fix UI accessibility violations with targeted, minimal patches covering ARIA attributes, semantic HTML, keyboard access, focus management, and form error linking.
- Open reference: `references/skills/fixing-accessibility.md`
- Open examples: `examples/skills/fixing-accessibility.md`

### fixing-metadata
- Summary: Audit and fix page metadata including titles, descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, structured data, and locale settings.
- Open reference: `references/skills/fixing-metadata.md`
- Open examples: `examples/skills/fixing-metadata.md`

### fixing-motion-performance
- Summary: Diagnose and fix animation performance issues including layout thrashing, composite layer promotion, FLIP patterns, scroll-linked motion, and reduced-motion preferences.
- Open reference: `references/skills/fixing-motion-performance.md`
- Open examples: `examples/skills/fixing-motion-performance.md`

### screen-reader-testing
- Summary: Test web applications with screen readers (VoiceOver, NVDA, JAWS, TalkBack) covering navigation, forms, dynamic content, modals, live regions, and tab interfaces.
- Open reference: `references/skills/screen-reader-testing.md`
- Open examples: `examples/skills/screen-reader-testing.md`

### ui-visual-validator
- Summary: Verify UI modifications, design system compliance, and accessibility implementation through systematic visual analysis with evidence-based assessment methodology.
- Open reference: `references/skills/ui-visual-validator.md`
- Open examples: `examples/skills/ui-visual-validator.md`

### wcag-audit-patterns
- Summary: Audit web content against WCAG 2.2 guidelines across all four POUR principles with automated tooling, manual checks, and actionable remediation strategies.
- Open reference: `references/skills/wcag-audit-patterns.md`
- Open examples: `examples/skills/wcag-audit-patterns.md`

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
