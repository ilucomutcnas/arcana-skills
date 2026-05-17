---
name: "design-systems"
title: "Design Systems"
description: "Use for building, governing, and reviewing production-grade design systems with enterprise token operations and adoption workflows."
version: "1.1.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Build, govern, and scale production-grade design systems across products and brands, including token lifecycle operations and organization-wide adoption programs.

## Domain Coverage

This package covers foundations, component contracts, theming, accessibility, documentation, governance, auditing, framework mapping, token lifecycle governance, and cross-team adoption playbooks.

## How to Use

1. Run self-diagnostic (`self-diagnostic-protocol.md`).
2. Pick a primary mini-skill and adjacent skills.
3. Use references for methods and examples for end-to-end patterns.
4. Use routing and catalog resources for composition.

## Multi-Skill Activation Guide

- New design system: foundations + components + theming + accessibility + documentation
- Enterprise token rollout: foundations + design-token-governance + theming + governance
- Component implementation: components + accessibility + framework-mapping
- Organizational rollout: governance + system-adoption-playbook + documentation
- Audit remediation program: review-audit + system-adoption-playbook + governance

## Package Structure

- `SKILL.md`
- `composition-protocol.md`
- `self-diagnostic-protocol.md`
- `resources/skill-catalog.md`
- `resources/routing-guide.md`
- `resources/asset-link-index.md`
- `resources/manifest.json`
- `references/skills/*.md`
- `examples/skills/*.md`
- `shared-rules/STYLE-GUARDRAILS.md`
- `shared-rules/ANTI-PATTERNS.md`

## Mini-Skills Index

### foundations
- Summary: Token primitives, semantic layers, naming conventions, and scale governance.
- Open reference: `references/skills/foundations.md`
- Open examples: `examples/skills/foundations.md`

### components
- Summary: Component API contracts, states, variants, slots, behavior modes, and handoff quality.
- Open reference: `references/skills/components.md`
- Open examples: `examples/skills/components.md`

### theming
- Summary: Light/dark/high-contrast/multi-brand semantic theme systems with inheritance and fallback discipline.
- Open reference: `references/skills/theming.md`
- Open examples: `examples/skills/theming.md`

### accessibility
- Summary: System-level accessibility governance across tokens, components, themes, and docs.
- Open reference: `references/skills/accessibility.md`
- Open examples: `examples/skills/accessibility.md`

### documentation
- Summary: Information architecture and decision-grade docs for usage, migration, and release communication.
- Open reference: `references/skills/documentation.md`
- Open examples: `examples/skills/documentation.md`

### governance
- Summary: Contribution, RFCs, ownership, release operations, and exceptions at package level.
- Open reference: `references/skills/governance.md`
- Open examples: `examples/skills/governance.md`

### review-audit
- Summary: Compliance scoring, risk prioritization, remediation backlog, and reporting.
- Open reference: `references/skills/review-audit.md`
- Open examples: `examples/skills/review-audit.md`

### framework-mapping
- Summary: Semantic token/component mapping to CSS variables, Tailwind, CSS Modules, and CSS-in-JS.
- Open reference: `references/skills/framework-mapping.md`
- Open examples: `examples/skills/framework-mapping.md`

### design-token-governance
- Summary: Token lifecycle operations from proposal to rollout, compatibility, CI validation, and migration safety.
- Open reference: `references/skills/design-token-governance.md`
- Open examples: `examples/skills/design-token-governance.md`

### system-adoption-playbook
- Summary: Multi-team adoption strategy, migration waves, enablement, metrics, and exceptions governance.
- Open reference: `references/skills/system-adoption-playbook.md`
- Open examples: `examples/skills/system-adoption-playbook.md`
