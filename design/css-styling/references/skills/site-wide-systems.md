---
name: "site-wide-systems"
title: "Site-Wide CSS Systems"
description: "Rules for styling consistency across large sites, multi-page products, shared themes, and long-term maintenance."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/site-wide-systems.md`
- Examples: `examples/skills/site-wide-systems.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# Site-Wide CSS Systems

## Purpose
Manage CSS as an operating system for a whole website or product family, not as isolated page decoration.

## Use when
- multiple pages must feel coherent
- multiple teams touch the same styling system
- theming or brand governance matters
- utility sprawl is becoming dangerous
- page-level drift has started

## System responsibilities

- token governance
- page template consistency
- shared component patterns
- dark mode / themes
- content typography system
- utility boundaries
- global exceptions policy

## Best practices

- Define canonical page templates.
- Create a spacing rhythm across the full site.
- Keep typography roles stable.
- Publish a small set of sanctioned utility helpers.
- Track ownership of global CSS.
- Use changelogs for token updates in serious projects.

## Bad practices

- homepage looks premium, inner pages look generic
- each team invents its own spacing
- no standard content width
- utilities act as permanent substitute for system design
- theme changes require hunting through component files

## Validation

- Would a new page inherit quality automatically?
- Are deviations intentional or accidental?
- Can brand refresh happen through variables and components rather than rewrites?
