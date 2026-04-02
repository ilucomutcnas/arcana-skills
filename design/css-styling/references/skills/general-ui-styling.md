---
name: "general-ui-styling"
title: "General UI CSS Styling"
description: "Rules for day-to-day UI styling: forms, cards, states, controls, density, hierarchy, and surface systems."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/general-ui-styling.md`
- Examples: `examples/skills/general-ui-styling.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# General UI CSS Styling

## Purpose
Handle normal product UI styling professionally: dashboards, settings pages, cards, forms, tables, modals, chips, filters, and content modules.

## Focus areas

### Visual hierarchy
- Make primary actions obvious.
- Keep supporting UI quiet.
- Use spacing before borders.
- Use contrast before decoration.

### Component states
Every meaningful component should define:
- default
- hover
- active / pressed
- focus-visible
- disabled
- error
- loading
- selected, if relevant

### Surface system
Define a clear relationship between:
- page background
- elevated surfaces
- interactive controls
- overlays
- destructive actions
- success / warning / info states

### Density discipline
Choose a density mode intentionally:
- compact
- standard
- relaxed

Do not mix density logic randomly across adjacent components.

## Good practices

- Use consistent padding families for similar components.
- Keep radii coherent across the product.
- Make forms feel deliberate, not assembled.
- Use border, background, and shadow sparingly but consistently.
- Ensure keyboard users can track focus.

## Bad practices

- every card styled differently
- hidden focus state
- hover that shifts layout
- excessive shadow stacking
- unreadable placeholder text
- overusing muted text until the interface loses hierarchy

## Output expectations

When producing CSS guidance:
- state the intended component contract
- define token dependencies
- define state behavior
- mention accessibility-critical styling when relevant
