---
name: "design-system-accessibility"
title: "Design System Accessibility"
description: "Bakes accessibility into tokens, components, theming, and documentation at the system level."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/accessibility.md`
- Examples: `examples/skills/accessibility.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Accessibility

## Purpose
Ensure the design system is accessibility-aware by default, not by exception.

## Scope
- color contrast
- semantic structure
- keyboard navigation
- focus visibility
- target size
- state communication
- motion sensitivity
- screen-reader support assumptions

## Rules
1. Color cannot be the only state signal.
2. Focus-visible patterns must be systemized.
3. Disabled components must remain understandable.
4. Motion must have reduced-motion alternatives.
5. Token choices must be tested against contrast requirements.
6. Documentation must state known accessibility constraints.

## Required checks
- contrast for text and UI boundaries
- focus order and focus visibility
- keyboard operability assumptions
- icon-only control labeling strategy
- touch target sizing

## Validation
- Can a product team adopt this system without creating predictable accessibility regressions?
