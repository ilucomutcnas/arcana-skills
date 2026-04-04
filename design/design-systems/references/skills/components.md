---
name: "design-system-components"
title: "Design System Components"
description: "Designs reusable component contracts, states, variants, and composition rules for a scalable UI library."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/components.md`
- Examples: `examples/skills/components.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Components

## Purpose
Turn foundations into reusable primitives and components.

## Scope
- primitives vs composites
- slots and composition
- states and transitions
- variants and size models
- interaction behavior
- layout responsibilities
- content rules
- iconography rules

## Rules
1. Components should expose intent, not implementation leakage.
2. Variants must express meaningful differences, not aesthetic improvisation.
3. Prefer:
   - `variant`
   - `size`
   - `tone`
   - `state`
   over many boolean props.
4. A component should not silently change layout behavior between contexts.
5. Required states must be documented and testable.
6. Destructive, disabled, loading, and focus-visible are not optional afterthoughts.

## Recommended component template
- Purpose
- Anatomy
- Props / API
- Variants
- States
- Accessibility notes
- Content guidance
- Do / Don't
- Example implementations

## Validation
- Can this component be reused in multiple products?
- Are states exhaustive enough?
- Does the API reduce custom forks?
