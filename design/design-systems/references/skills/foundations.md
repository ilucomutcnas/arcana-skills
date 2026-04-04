---
name: "design-system-foundations"
title: "Design System Foundations"
description: "Defines the visual and semantic foundation of a design system: tokens, scales, primitives, and naming."
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

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Foundations

## Purpose
Define the base language of the system before components are designed.

## Scope
- color system and semantic mapping
- typography roles
- spacing scale
- radii
- shadows / elevation
- borders and strokes
- grid and breakpoints
- motion primitives
- z-layer model

## Rules
1. Tokens represent **roles**, not temporary taste.
2. Prefer semantic layers:
   - global/base tokens
   - alias/semantic tokens
   - component tokens only when required
3. Color tokens must separate:
   - primitive palette
   - semantic meaning
   - surface usage
4. Typography tokens should describe role and behavior, not page names.
5. Spacing must use a coherent scale. Arbitrary values are exceptions, not defaults.
6. Motion belongs in the system only if timing and easing are reused.

## Deliverables
- token inventory
- naming model
- usage rules
- edge-case notes
- implementation mapping

## Validation
- Can another team infer where to use each token?
- Can the system survive a rebrand without rewriting every component?
- Are accessibility constraints compatible with token choices?
