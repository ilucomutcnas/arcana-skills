---
name: "accessibility-ux"
title: "Accessibility & UX Standards"
description: "Use for WCAG compliance audits, accessibility fixes, screen reader testing, UI visual validation, motion performance optimization, metadata governance, and assistive technology edge-case triage."
version: "1.0.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide structured guidance for building, auditing, validating, and reporting accessible web experiences with WCAG 2.2 mapping, assistive technology evidence, remediation governance, and retest-ready outputs.

## Domain Coverage

This package covers accessibility remediation, metadata accessibility context, motion safety, screen reader workflows, visual validation, WCAG audit methodology, audit reporting governance, and cross-assistive-technology edge-case triage.

## How to Use

1. Run `self-diagnostic-protocol.md` checks for package integrity and evidence readiness.
2. Select the primary mini-skill for the request.
3. Use the Multi-Skill Activation Guide to load adjacent and validation mini-skills.
4. Open `references/skills/<slug>.md` for method and guardrails.
5. Open `examples/skills/<slug>.md` for realistic end-to-end workflows.
6. Use `resources/routing-guide.md` for multi-skill routing.
7. Use `resources/asset-link-index.md` to preserve all linked resources.

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
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `shared-rules/STYLE-GUARDRAILS.md` — package-wide output guardrails
- `shared-rules/ANTI-PATTERNS.md` — package-wide rejection checks
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted code snippets and usage samples

## Mini-Skills Index

### fixing-accessibility
- Summary: Remediate component-level accessibility failures for forms, dialogs, menus, tabs, accordions, icon-only controls, live regions, and focus recovery.
- Open reference: `references/skills/fixing-accessibility.md`
- Open examples: `examples/skills/fixing-accessibility.md`

### fixing-metadata
- Summary: Fix metadata impacting accessible naming context, locale routing, social preview fidelity, canonical integrity, and structured content meaning.
- Open reference: `references/skills/fixing-metadata.md`
- Open examples: `examples/skills/fixing-metadata.md`

### fixing-motion-performance
- Summary: Resolve animation jank and vestibular risk with reduced-motion paths, safe transition constraints, and dynamic focus/scroll protections.
- Open reference: `references/skills/fixing-motion-performance.md`
- Open examples: `examples/skills/fixing-motion-performance.md`

### screen-reader-testing
- Summary: Run scripted screen reader tests across VoiceOver/NVDA/JAWS/TalkBack with mode-specific checks for forms, dialogs, tabs, and live updates.
- Open reference: `references/skills/screen-reader-testing.md`
- Open examples: `examples/skills/screen-reader-testing.md`

### ui-visual-validator
- Summary: Validate focus visibility, contrast, hit targets, zoom/text-spacing behavior, and responsive stability after accessibility changes.
- Open reference: `references/skills/ui-visual-validator.md`
- Open examples: `examples/skills/ui-visual-validator.md`

### wcag-audit-patterns
- Summary: Execute WCAG 2.2 methodology including sampling, criterion mapping, manual and automated checks, and remediation sequencing.
- Open reference: `references/skills/wcag-audit-patterns.md`
- Open examples: `examples/skills/wcag-audit-patterns.md`

### wcag-audit-reporting
- Summary: Build compliance-ready audit deliverables with severity scoring, evidence packs, owner assignment, retest workflow, and stakeholder summaries.
- Open reference: `references/skills/wcag-audit-reporting.md`
- Open examples: `examples/skills/wcag-audit-reporting.md`

### assistive-tech-edge-cases
- Summary: Investigate edge failures across speech/switch input, magnification, forced colors, zoom, gesture conflicts, and dynamic-update traps.
- Open reference: `references/skills/assistive-tech-edge-cases.md`
- Open examples: `examples/skills/assistive-tech-edge-cases.md`

## Validation

- Keep implementation depth in reference/example files.
- Preserve existing mini-skill semantics and resource links.
- Require evidence-backed accessibility claims before final recommendations.

## Output Requirements

- Keep this file concise and navigational.
- Route detailed workflows to extracted references/examples.
- Preserve stable slugs and file names.
