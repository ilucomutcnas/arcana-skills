---
name: "design-md"
title: "Design MD"
description: "Use for creating DESIGN.md files as design system documentation for Stitch projects, capturing visual themes, color palettes, typography, component styles, and layout principles."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure
- Main router: `SKILL.md`
- This reference: `references/skills/design-md.md`
- Examples: `examples/skills/design-md.md`

## Linked Package Files
- Adjacent: `references/skills/brand-bible.md` — for brand voice in design documentation
- Adjacent: `references/skills/brand-guidelines-anthropic.md` — for brand color/typography reference
- Validation: `references/skills/web-design-codex.md` — for web interface guideline alignment

## Purpose
Create DESIGN.md files that serve as the source of truth for prompting Stitch to generate new screens matching an existing design language. Stitch interprets design through visual descriptions supported by specific color values. This skill analyzes existing screens and synthesizes a semantic design system document.

## When to Use
- When analyzing Stitch projects
- When creating DESIGN.md files for design-to-code workflows
- When synthesizing semantic design systems from existing screens
- When generating design documentation for Stitch projects

## Workflow
1. Retrieve project information from the Stitch MCP Server.
2. Get screen details: code, image, and screen object information.
3. Reference the Stitch Effective Prompting Guide.
4. Extract design tokens from the screen and translate to descriptive language.
5. Generate the DESIGN.md file following the prescribed structure.

## Quality Standards
- Be descriptive — use "Ocean-deep Cerulean (#0077B6)" not just "blue".
- Be functional — explain what each design element is used for.
- Be consistent — use the same terminology throughout.
- Be visual — help readers visualize the design through descriptions.
- Be precise — include exact values (hex codes, pixel values) in parentheses after natural language.

## Technical Rules
- Requires access to the Stitch MCP Server.
- Requires a Stitch project with at least one designed screen.
- Reference the Stitch Effective Prompting Guide at: https://stitch.withgoogle.com/docs/learn/prompting/
- Use descriptive design terminology and natural language exclusively.
- Include exact hex codes for colors alongside descriptive names.

## Validation
- Verify the DESIGN.md follows the prescribed section structure.
- Confirm all color values include both descriptive names and hex codes.
- Check that component stylings are specific and functional.

## Restrictions
- Do not use generic terms ("blue", "rounded") without descriptive qualification.
- Do not omit exact values when describing design tokens.

## Output Requirements
- Clean markdown file following the DESIGN.md structure.
- All sections: Visual Theme, Color Palette, Typography Rules, Component Stylings, Layout Principles.
- Descriptive language with precise values throughout.
