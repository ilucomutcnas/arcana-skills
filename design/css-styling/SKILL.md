---
name: "css-styling"
title: "CSS & Styling Systems"
description: "Use for CSS architecture, design tokens, layout systems, responsive design, UI styling, animation, Tailwind/SCSS/CSS Modules guidance, CSS review and audit, one-pager and landing page styling, site-wide consistency, naming conventions, frontend design engineering, and React/TypeScript frontend development guidelines."
version: "1.0.0"
category: "Frontend"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide structured, opinionated guidance for CSS and frontend styling across all scales — from token systems and layout primitives to full-site consistency and React application architecture. This domain prevents AI-generated interface slop by enforcing professional styling standards, maintainable architecture, and framework-aware best practices.

## Domain Coverage

This package represents the CSS and styling systems domain. It covers token architecture, layout and responsive design, UI component styling, animation and motion, framework-specific guidance, naming conventions, landing page styling, site-wide systems, CSS auditing, Tailwind design systems, frontend design engineering, and React/TypeScript development guidelines.

Shared guardrails in `shared-rules/STYLE-GUARDRAILS.md` and anti-patterns in `shared-rules/ANTI-PATTERNS.md` apply across all mini-skills.

## How to Use

1. Always begin with self-diagnostic. Start with a quick package integrity check, then validate only the activated working set. The self-diagnostic rules are defined in `self-diagnostic-protocol.md`.
2. Identify the primary mini-skill that best matches the task.
3. Check the Multi-Skill Activation Guide below to load adjacent mini-skills.
4. Open the corresponding reference file under `references/skills/`.
5. Open the corresponding examples file under `examples/skills/` if concrete patterns are needed.
6. Use `resources/skill-catalog.md` for the full index.
7. Use `resources/routing-guide.md` when a task spans multiple mini-skills.
8. Use `resources/asset-link-index.md` to find every auxiliary folder and file.

## Multi-Skill Activation Guide

Common combinations:

- **New design system**: foundations (primary) + framework-guides + general-ui-styling + tailwind-design-system
- **Component styling**: general-ui-styling (primary) + foundations + animation-motion + css-review-audit
- **Landing page**: one-pager-landing (primary) + layout-responsive + animation-motion + general-ui-styling
- **Layout work**: layout-responsive (primary) + foundations + general-ui-styling
- **CSS audit**: css-review-audit (primary) + foundations + framework-guides + site-wide-systems
- **Tailwind project**: tailwind-design-system (primary) + framework-guides + foundations + general-ui-styling
- **React application**: frontend-dev-guidelines (primary) + frontend-alchemy + tailwind-design-system + general-ui-styling
- **Site-wide consistency**: site-wide-systems (primary) + foundations + layout-responsive + language-conventions
- **Animation system**: animation-motion (primary) + general-ui-styling + foundations
- **Design engineering**: frontend-alchemy (primary) + general-ui-styling + animation-motion + layout-responsive

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
- `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

## Mini-Skills Index

### foundations
- Summary: Define the base doctrine for tokens, cascade, naming, theming, layering, and maintainable CSS system design.
- Open reference: `references/skills/foundations.md`
- Open examples: `examples/skills/foundations.md`

### layout-responsive
- Summary: Production rules for layout primitives, spacing systems, breakpoints, fluid design, and responsive consistency.
- Open reference: `references/skills/layout-responsive.md`
- Open examples: `examples/skills/layout-responsive.md`

### general-ui-styling
- Summary: Rules for day-to-day UI styling: forms, cards, states, controls, density, hierarchy, and surface systems.
- Open reference: `references/skills/general-ui-styling.md`
- Open examples: `examples/skills/general-ui-styling.md`

### animation-motion
- Summary: Tasteful, performance-safe motion for UI content transitions, interactive states, and reduced-motion support.
- Open reference: `references/skills/animation-motion.md`
- Open examples: `examples/skills/animation-motion.md`

### one-pager-landing
- Summary: CSS doctrine for landing pages, promo pages, hero sections, CTA styling, and conversion-oriented surfaces.
- Open reference: `references/skills/one-pager-landing.md`
- Open examples: `examples/skills/one-pager-landing.md`

### site-wide-systems
- Summary: Rules for styling consistency across large sites, multi-page products, shared themes, and long-term maintenance.
- Open reference: `references/skills/site-wide-systems.md`
- Open examples: `examples/skills/site-wide-systems.md`

### css-review-audit
- Summary: Structured workflow for reviewing CSS, identifying anti-patterns by severity, and proposing concrete fixes.
- Open reference: `references/skills/css-review-audit.md`
- Open examples: `examples/skills/css-review-audit.md`

### framework-guides
- Summary: Framework-aware guidance for vanilla CSS, SCSS, Tailwind, CSS Modules, and CSS-in-JS without mixing rules blindly.
- Open reference: `references/skills/framework-guides.md`
- Open examples: `examples/skills/framework-guides.md`

### language-conventions
- Summary: Rules for CSS naming, comments, mixed-language teams, and multilingual codebases.
- Open reference: `references/skills/language-conventions.md`
- Open examples: `examples/skills/language-conventions.md`

### frontend-alchemy
- Summary: Create memorable, high-craft frontend interfaces with intentional aesthetic direction, technical correctness, and cohesive restraint.
- Open reference: `references/skills/frontend-alchemy.md`
- Open examples: `examples/skills/frontend-alchemy.md`

### tailwind-design-system
- Summary: Build production-ready design systems with Tailwind CSS including tokens, component variants, semantic colors, shadcn/ui patterns, dark mode, and accessibility.
- Open reference: `references/skills/tailwind-design-system.md`
- Open examples: `examples/skills/tailwind-design-system.md`

### frontend-dev-guidelines
- Summary: Production-grade React/TypeScript development with Suspense-first data fetching, feature-based organization, strict TypeScript, and performance-safe defaults.
- Open reference: `references/skills/frontend-dev-guidelines.md`
- Open examples: `examples/skills/frontend-dev-guidelines.md`

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
