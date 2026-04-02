---
name: "theme-factory"
title: "Theme Factory"
description: "Use for applying consistent, professional themes with cohesive color palettes and font pairings to slide decks and artifacts from 10 pre-built themes."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure
- Main router: `SKILL.md`
- This reference: `references/skills/theme-factory.md`
- Examples: `examples/skills/theme-factory.md`
- Theme definitions: `theme-factory__themes/` (10 .md files)
- Theme showcase PDF: `theme-factory__theme-showcase.pdf`
- License: `theme-factory__LICENSE.txt`

## Linked Package Files
- Adjacent: `references/skills/brand-guidelines-anthropic.md` — for brand-aligned theming
- Adjacent: `references/skills/canvas-design.md` — for visual artifact theming
- Validation: `references/skills/design-orchestration.md` — for design workflow integration

## Purpose
Apply consistent, professional styling to presentation slide decks and other artifacts. Provides 10 pre-built themes, each with a cohesive color palette, complementary font pairings, and a distinct visual identity for different contexts and audiences.

## When to Use
- When styling presentation slide decks
- When applying visual themes to artifacts or documents
- When selecting from pre-built color and typography combinations
- When a user needs to preview and choose a theme

## Workflow
1. Show the theme showcase: display `theme-factory__theme-showcase.pdf` to allow the user to see all available themes visually. Do not modify it — simply show it for viewing.
2. Ask for the user's choice.
3. Wait for explicit confirmation of the chosen theme.
4. Apply the selected theme's colors and fonts to the deck or artifact.

Available themes (see `theme-factory__themes/` for definitions):
Arctic Frost, Botanical Garden, Desert Rose, Forest Canopy, Golden Hour, Midnight Galaxy, Modern Minimalist, Ocean Depths, Sunset Boulevard, Tech Innovation.

## Quality Standards
- Apply the full theme consistently: colors, fonts, and visual identity.
- Do not mix elements from different themes.
- Ensure text remains readable against theme backgrounds.

## Technical Rules
- Each theme file in `theme-factory__themes/` defines: color palette (hex codes), typography (header and body fonts), and best-use contexts.
- Fonts: primarily DejaVu Sans, DejaVu Serif, and their bold variants.
- Read the specific theme .md file for exact values before applying.

## Validation
- Verify all theme colors are applied correctly.
- Confirm font pairings match the theme definition.
- Check text readability against all backgrounds.

## Restrictions
- Do not modify the theme-showcase.pdf.
- Do not mix themes within a single artifact unless explicitly requested.

## Output Requirements
- Themed artifact with consistent color and typography.
- Note which theme was applied.
