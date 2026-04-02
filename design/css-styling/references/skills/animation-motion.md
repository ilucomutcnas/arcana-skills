---
name: "animation-motion"
title: "CSS Animation & Motion Systems"
description: "Tasteful, performance-safe motion for UI content transitions, interactive states, and reduced-motion support."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/animation-motion.md`
- Examples: `examples/skills/animation-motion.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# CSS Animation & Motion Systems

## Purpose
Use motion to clarify interface behavior, reinforce hierarchy, and add tactility without harming performance or trust.

## Motion doctrine

### Motion is functional first
Motion should:
- indicate change
- confirm interaction
- guide attention
- preserve orientation
- soften state transitions

It should not:
- distract
- delay obvious tasks
- simulate depth everywhere
- constantly compete with content

### Safe defaults
Prefer animating:
- opacity
- transform

Avoid animating when possible:
- width
- height
- top
- left
- filter on large surfaces
- box-shadow on many items at once

### Duration guidance
- tiny feedback: 100–140ms
- standard interaction: 160–220ms
- panel / overlay motion: 220–320ms
- major decorative sequences: only when justified

### Reduced motion
Always provide a reduced-motion path.

## Good practices

- Use one or two easing families consistently.
- Match motion intensity to component importance.
- Keep list hover effects subtle.
- Make skeletons and loading feedback calm, not flashy.

## Bad practices

- bounce everywhere
- oversized spring motion for enterprise UI
- delayed hover response
- infinite pulsing on critical surfaces
- entrance animation on every element in a dense screen

## Validation

Ask:
- Does this help comprehension?
- Is this performant on low-end hardware?
- Would turning this off improve usability?
- Is reduced motion respected?
