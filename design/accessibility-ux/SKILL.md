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
Provide structured guidance for building, auditing, and fixing accessible web interfaces with production-grade reporting and cross-assistive-technology reliability checks.

## Domain Coverage
This package covers WCAG 2.2 audit methodology, accessibility remediation, metadata accessibility context, motion safety, screen reader testing, visual verification, audit reporting governance, and assistive-technology edge-case triage.

## How to Use
1. Start with `self-diagnostic-protocol.md`.
2. Select a primary mini-skill.
3. Activate adjacent and validation mini-skills using the Multi-Skill Activation Guide.
4. Open `references/skills/<slug>.md` for workflow and quality gates.
5. Open `examples/skills/<slug>.md` for end-to-end project patterns.
6. Use `resources/routing-guide.md` for multi-skill routing.
7. Use `resources/asset-link-index.md` to preserve linked resource folders.

## Multi-Skill Activation Guide
- **Accessibility audit report**: wcag-audit-reporting (primary) + wcag-audit-patterns + screen-reader-testing + ui-visual-validator
- **Assistive-tech edge-case investigation**: assistive-tech-edge-cases (primary) + screen-reader-testing + fixing-accessibility + ui-visual-validator
- **Remediation program**: fixing-accessibility (primary) + wcag-audit-reporting + wcag-audit-patterns + screen-reader-testing
- **Motion accessibility risk**: fixing-motion-performance (primary) + assistive-tech-edge-cases + fixing-accessibility
- **Full accessibility audit**: wcag-audit-patterns (primary) + fixing-accessibility + screen-reader-testing + ui-visual-validator
- **Metadata and route UX validation**: fixing-metadata (primary) + ui-visual-validator + wcag-audit-reporting

## Package Structure
- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — package self-diagnostic rules
- `resources/skill-catalog.md` — full mini-skill index
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — link map for auxiliary folders and files
- `resources/manifest.json` — machine-readable package manifest
- `shared-rules/STYLE-GUARDRAILS.md` — package-wide output guardrails
- `shared-rules/ANTI-PATTERNS.md` — package-wide rejection checklist
- `references/skills/*.md` — extracted guidance per mini-skill
- `examples/skills/*.md` — extracted workflow examples

## Mini-Skills Index
### fixing-accessibility
- Summary: Fix component-level violations for dialogs, forms, menus, tabs, accordions, icon-only buttons, live regions, and focus recovery.
- Open reference: `references/skills/fixing-accessibility.md`
- Open examples: `examples/skills/fixing-accessibility.md`
### fixing-metadata
- Summary: Fix metadata quality for accessible titles, route context, locale alternates, social previews, canonical integrity, and structured data.
- Open reference: `references/skills/fixing-metadata.md`
- Open examples: `examples/skills/fixing-metadata.md`
### fixing-motion-performance
- Summary: Resolve motion and performance risks with reduced-motion safeguards, stable focus behavior, and low-jank interaction design.
- Open reference: `references/skills/fixing-motion-performance.md`
- Open examples: `examples/skills/fixing-motion-performance.md`
### screen-reader-testing
- Summary: Run structured VoiceOver/NVDA/JAWS/TalkBack scripts including focus mode and virtual cursor checks.
- Open reference: `references/skills/screen-reader-testing.md`
- Open examples: `examples/skills/screen-reader-testing.md`
### ui-visual-validator
- Summary: Validate focus visibility, contrast, hit targets, zoom, text spacing, dark mode, and forced-colors output.
- Open reference: `references/skills/ui-visual-validator.md`
- Open examples: `examples/skills/ui-visual-validator.md`
### wcag-audit-patterns
- Summary: Execute WCAG 2.2 methodology with sampling, criterion mapping, severity interpretation, and remediation sequencing.
- Open reference: `references/skills/wcag-audit-patterns.md`
- Open examples: `examples/skills/wcag-audit-patterns.md`
### wcag-audit-reporting
- Summary: Produce compliance-ready audit reporting with evidence packs, owner assignments, remediation backlog governance, and retest tracking.
- Open reference: `references/skills/wcag-audit-reporting.md`
- Open examples: `examples/skills/wcag-audit-reporting.md`
### assistive-tech-edge-cases
- Summary: Diagnose failures that surface only in AT/input/setting combinations beyond baseline screen reader checks.
- Open reference: `references/skills/assistive-tech-edge-cases.md`
- Open examples: `examples/skills/assistive-tech-edge-cases.md`

## Validation
- Keep detailed execution guidance in reference/example files.
- Preserve all existing mini-skill slugs and linked resources.
- Require evidence-backed conclusions for every accessibility claim.

## Output Requirements
- Keep `SKILL.md` concise and navigational.
- Route deep guidance to extracted files.
- Preserve stable mini-skill slugs and file names.
