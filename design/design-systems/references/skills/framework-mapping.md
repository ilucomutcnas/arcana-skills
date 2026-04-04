---
name: "design-system-framework-mapping"
title: "Design System Framework Mapping"
description: "Maps design-system concepts to CSS, Tailwind, CSS Modules, utility-first systems, and CSS-in-JS without losing semantic intent."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/framework-mapping.md`
- Examples: `examples/skills/framework-mapping.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Framework Mapping

## Purpose
Translate design-system concepts into implementation patterns without collapsing semantics into random classes.

## Scope
- plain CSS
- SCSS
- CSS Modules
- Tailwind
- CSS-in-JS
- component-library token mapping

## Rules
1. Framework choice does not excuse semantic drift.
2. Tokens must remain source-of-truth regardless of implementation style.
3. Utility classes may express layout quickly, but semantic roles still need stable mapping.
4. CSS-in-JS is not a substitute for a system model.
5. Tailwind projects still need token discipline and variant discipline.

## Mapping guidance
### Plain CSS / SCSS
- Prefer CSS custom properties for tokens.
- Separate token layer from component layer.

### CSS Modules
- Use modules for local component styling, not for redefining global token meaning.

### Tailwind
- Extend the theme with semantic tokens.
- Avoid spraying raw utility values when a system token exists.
- Use component abstractions for repeated patterns.

### CSS-in-JS
- Keep token access centralized.
- Avoid ad hoc inline objects that drift from system naming.

## Validation
- Can design decisions be traced from system token to rendered UI regardless of stack?
