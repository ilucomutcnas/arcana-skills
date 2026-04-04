---
name: "design-system-theming"
title: "Design System Theming"
description: "Defines multi-theme, light/dark, and multi-brand theming with semantic safety and implementation discipline."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/theming.md`
- Examples: `examples/skills/theming.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Theming

## Purpose
Create theming models that scale across brands, modes, and accessibility constraints.

## Scope
- light/dark themes
- brand themes
- semantic color contracts
- high-contrast strategies
- mode-safe illustrations and surfaces
- theme extension and override policy

## Rules
1. Themes change token values, not component meaning.
2. Semantic tokens must remain stable across themes.
3. Do not hardcode dark-mode overrides inside components when a semantic token can solve it.
4. Brand customization should happen through tokens first, components second.
5. Every theme must be validated for contrast, focus visibility, and status colors.

## Recommended theme model
- primitives
- semantic aliases
- component aliases where strictly needed
- runtime theme selection strategy
- fallback behavior

## Validation
- Can a new brand be added without component rewrites?
- Do themes preserve meaning for success/warning/destructive states?
- Does reduced motion remain respected across themes?
