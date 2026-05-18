---
name: "design-systems"
title: "Design Systems"
description: "Use for building, governing, and reviewing production-grade design systems. Covers tokens, foundations, components, theming, accessibility, documentation, governance, auditing, framework mapping, token lifecycle governance, and enterprise adoption workflows."
version: "1.1.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Build, govern, and review production-grade design systems. This domain covers the full lifecycle: foundational tokens and scales, reusable component contracts, theming and multi-brand support, accessibility baked into the system level, documentation for adoption, governance for sustainability, auditing for compliance, framework mapping for implementation, token lifecycle governance, and organizational adoption playbooks.

## Domain Coverage

This package represents the design systems domain. It covers interconnected capabilities that must work together: foundations define the visual language, components consume it, theming adapts it, accessibility constrains it, documentation communicates it, governance protects it, auditing enforces it, framework mapping implements it, design-token-governance manages token lifecycle safety, and system-adoption-playbook drives cross-team rollout.

Shared guardrails in `shared-rules/STYLE-GUARDRAILS.md` and anti-patterns in `shared-rules/ANTI-PATTERNS.md` apply across all mini-skills.

## How to Use

1. Always begin with self-diagnostic per `self-diagnostic-protocol.md`.
2. Identify the primary mini-skill that best matches the task.
3. Check the Multi-Skill Activation Guide below.
4. Open the corresponding reference under `references/skills/`.
5. Open examples under `examples/skills/` if concrete patterns are needed.
6. Use `resources/skill-catalog.md` for the full index.
7. Use `resources/routing-guide.md` when a task spans multiple mini-skills.

## Multi-Skill Activation Guide

Common combinations:

- **New design system**: foundations (primary) + components + theming + accessibility + documentation
- **Component library**: components (primary) + foundations + accessibility + framework-mapping
- **Theming and dark mode**: theming (primary) + foundations + accessibility
- **System audit**: review-audit (primary) + foundations + components + governance
- **Implementation mapping**: framework-mapping (primary) + foundations + components
- **Governance setup**: governance (primary) + documentation + review-audit
- **Accessibility review**: accessibility (primary) + components + theming + review-audit
- **Enterprise token rollout**: design-token-governance (primary) + foundations + theming + governance
- **Organizational rollout**: system-adoption-playbook (primary) + governance + documentation
- **Audit remediation program**: review-audit (primary) + system-adoption-playbook + governance

## Package Structure

- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted examples and patterns per mini-skill
- `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns reference

## Mini-Skills Index

### foundations
- Summary: Defines visual and semantic foundations: token primitives, aliasing strategy, naming conventions, scales, and foundation QA.
- Open reference: `references/skills/foundations.md`
- Open examples: `examples/skills/foundations.md`

### components
- Summary: Designs reusable component contracts, variants, states, slots, and controlled/uncontrolled behavior for scalable UI libraries.
- Open reference: `references/skills/components.md`
- Open examples: `examples/skills/components.md`

### theming
- Summary: Defines light/dark/high-contrast/multi-brand theming with semantic mapping, inheritance, fallback, and regression control.
- Open reference: `references/skills/theming.md`
- Open examples: `examples/skills/theming.md`

### accessibility
- Summary: Bakes accessibility into tokens, components, theming, and documentation with system-level governance and evidence.
- Open reference: `references/skills/accessibility.md`
- Open examples: `examples/skills/accessibility.md`

### documentation
- Summary: Documents system intent, usage rules, migration notes, and component contracts for mixed design/engineering audiences.
- Open reference: `references/skills/documentation.md`
- Open examples: `examples/skills/documentation.md`

### governance
- Summary: Defines contribution, review gates, ownership, versioning, deprecation, and release operations for sustainable systems.
- Open reference: `references/skills/governance.md`
- Open examples: `examples/skills/governance.md`

### review-audit
- Summary: Audits products and libraries against system rules, scoring risk and prioritizing remediation.
- Open reference: `references/skills/review-audit.md`
- Open examples: `examples/skills/review-audit.md`

### framework-mapping
- Summary: Maps tokens/components to CSS variables, Tailwind, CSS Modules, and CSS-in-JS without losing semantic intent.
- Open reference: `references/skills/framework-mapping.md`
- Open examples: `examples/skills/framework-mapping.md`

### design-token-governance
- Summary: Governs token lifecycle operations: proposal, classification, compatibility, deprecation, migration, CI gates, and release safety.
- Open reference: `references/skills/design-token-governance.md`
- Open examples: `examples/skills/design-token-governance.md`

### system-adoption-playbook
- Summary: Guides organization-wide system rollout through stakeholder alignment, migration waves, enablement, metrics, and exception governance.
- Open reference: `references/skills/system-adoption-playbook.md`
- Open examples: `examples/skills/system-adoption-playbook.md`

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
