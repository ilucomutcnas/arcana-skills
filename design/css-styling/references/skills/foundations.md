---
name: "css-foundations"
title: "CSS Foundations & Architecture"
description: "Defines the base doctrine for tokens, cascade, naming, theming, layering, and maintainable CSS system design."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/foundations.md`
- Examples: `examples/skills/foundations.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# CSS Foundations & Architecture

## Purpose
Build a styling foundation that can scale without collapsing into overrides, duplication, and specificity fights.

## Use when
- creating or refactoring a design token system
- defining global styling rules
- deciding naming strategy
- setting cascade policy
- planning themes or dark mode
- establishing utility vs component boundaries

## Doctrine

### 1. Tokens first
Define and reuse tokens for:
- color
- spacing
- typography scale
- radius
- shadow
- border widths
- motion durations
- easing curves
- z-index layers

### 2. Stable layering
Use a clear order:
1. reset / normalize
2. tokens / variables
3. base elements
4. layout primitives
5. components
6. utilities
7. exceptions

### 3. Specificity must stay boring
- Prefer single-class selectors.
- Avoid tag-plus-class unless needed.
- Avoid nesting that creates accidental lock-in.
- Prefer local override contracts instead of selector escalation.

### 4. Theme through variables
Dark mode, brand mode, seasonal themes, or tenant-level branding should flow through variables, not duplicated selector trees.

### 5. Naming is operational
Choose a naming strategy and stay consistent:
- semantic component classes
- utility classes
- BEM-like structure
- token references
Do not combine them randomly.

## Good practices

- Use CSS custom properties for system values.
- Separate semantic tokens from raw palette values.
- Keep global CSS intentionally small.
- Document layer ownership clearly.
- Create layout primitives such as container, stack, cluster, grid, section.

## Bad practices

- random hardcoded colors
- spacing values invented per component
- z-index numbers without scale
- component styles dependent on page DOM structure
- unbounded nesting in preprocessors
- “temporary” overrides left in production

## Validation

Before finalizing:
- Can another page reuse this without override debt?
- Is the token system expressive enough but not bloated?
- Does dark mode or theming require duplication?
- Would deleting one file unexpectedly break three unrelated surfaces?
