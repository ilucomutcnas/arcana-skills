---
name: "framework-guides"
title: "CSS Framework & Method Guides"
description: "Framework-aware guidance for vanilla CSS, SCSS, Tailwind, CSS Modules, and CSS-in-JS without mixing rules blindly."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/framework-guides.md`
- Examples: `examples/skills/framework-guides.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# CSS Framework & Method Guides

## Purpose
Apply the right styling rules for the actual technology in use.

## Framework branches

### Plain CSS
Use for:
- global tokens
- base styles
- stable platform-wide rules
- high portability

### SCSS / Sass
Use when nesting, mixins, and partials genuinely improve maintainability.
Do not use SCSS as a license for selector bloat.

### CSS Modules
Use when component scoping is valuable and naming collisions must disappear.
Prefer explicit local contracts over cryptic local class sprawl.

### Tailwind
Use when utility-driven composition is already the project standard.
Still require:
- token discipline
- semantic patterns
- component consistency
- utility restraint

### CSS-in-JS
Use when styling truly depends on runtime state, theme context, or component API composition.
Avoid when static CSS would be simpler and faster.

## Selection guidance

Choose the smallest system that fits:
- use plain CSS for foundation
- use modules for scoped components
- use Tailwind where utility composition is already institutionalized
- use CSS-in-JS only where runtime styling needs justify it

## Forbidden behavior

- Do not paste rules from one methodology into another without adaptation.
- Do not combine Tailwind, giant SCSS globals, and ad hoc inline styles with no ownership model.
- Do not use framework preference as a substitute for system quality.
