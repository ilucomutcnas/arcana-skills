---
name: "layout-responsive"
title: "CSS Layout & Responsive Systems"
description: "Production rules for layout primitives, spacing systems, breakpoints, fluid design, and responsive consistency."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/layout-responsive.md`
- Examples: `examples/skills/layout-responsive.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# CSS Layout & Responsive Systems

## Purpose
Design layouts that scale across devices without ad hoc patching.

## Core doctrine

### 1. Start with layout primitives
Use reusable patterns:
- container
- section
- stack
- inline / cluster
- sidebar
- grid
- cover
- split hero

### 2. Responsive behavior should be systemic
Define:
- breakpoint philosophy
- max-width strategy
- spacing scale adaptation
- typography scaling
- layout collapse rules

### 3. Prefer fluid before fragmented
Use:
- `clamp()`
- fluid widths
- intrinsic sizing
- auto-fit / auto-fill grids
Before adding many breakpoint branches.

### 4. Mobile-first, but not mobile-blind
Start from constrained conditions, then expand.
But still optimize for the dominant real usage context of the product.

## Good practices

- Keep breakpoint count restrained.
- Use content-driven breakpoints where possible.
- Maintain readable line lengths.
- Treat spacing rhythm as part of responsiveness.
- Prevent overflow by design, not emergency patches.

## Bad practices

- too many breakpoints
- layout fixed by per-page exceptions
- arbitrary widths with no container logic
- text blocks stretching across giant monitors
- mobile solved with `overflow-x: auto` as the default rescue plan

## Review checklist

- Does the layout collapse gracefully?
- Are gaps and padding scaled intentionally?
- Does the hero still make sense on narrow screens?
- Are grids resilient to content variance?
