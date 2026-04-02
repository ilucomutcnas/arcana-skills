---
name: "brand-visual"
title: "Brand & Visual Design"
description: "Use for brand identity, visual design systems, ad creative copy, brand voice guidelines, canvas art, design documentation, theme styling, web interface reviews, and design workflow orchestration. Covers brand colors, typography, copy generation, design philosophies, and security-aware API design review."
version: "1.0.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide structured guidance for brand identity, visual design, ad creative production, design documentation, and design workflow management. This domain covers performance ad copy, brand voice, Anthropic brand guidelines, visual canvas art, design system documentation, presentation theming, web interface compliance, and design orchestration.

## Domain Coverage

This package represents the brand and visual design domain. It covers multiple interconnected capabilities: generating ad creative, defining brand voice, applying brand guidelines, creating visual art on canvas, documenting design systems, theming presentations, reviewing web interfaces against design standards, and orchestrating design workflows.

Mini-skills are separated for routing and selective loading. Real tasks in this domain often combine brand guidelines with creative output, or design documentation with visual validation.

## How to Use

1. Always begin with self-diagnostic. Start with a quick package integrity check, then validate only the activated working set. The self-diagnostic rules are defined in `self-diagnostic-protocol.md`.
2. Identify the primary mini-skill that best matches the task.
3. Check the Multi-Skill Activation Guide below to load adjacent mini-skills.
4. Open the corresponding reference file under `references/skills/`.
5. Open the corresponding examples file under `examples/skills/` if concrete patterns are needed.
6. Use `resources/skill-catalog.md` for the full index.
7. Use `resources/routing-guide.md` when a task spans multiple mini-skills.
8. Use `resources/asset-link-index.md` to find every auxiliary folder and file.

## Multi-Skill Activation Guide

Do not treat mini-skills as isolated when the task spans multiple concerns. For all non-trivial tasks, apply the universal composition rule in `composition-protocol.md`.

Common combinations:

- **Creating branded ad copy**: ad-creative (primary) + brand-bible + brand-guidelines-anthropic
- **Applying brand identity**: brand-guidelines-anthropic (primary) + brand-bible + canvas-design
- **Visual art creation**: canvas-design (primary) + theme-factory + brand-guidelines-anthropic
- **Design system documentation**: design-md (primary) + brand-bible + web-design-codex
- **Theming a presentation**: theme-factory (primary) + brand-guidelines-anthropic + canvas-design
- **Design workflow management**: design-orchestration (primary) + design-md + web-design-codex
- **Web interface review**: web-design-codex (primary) + brand-bible + brand-guidelines-anthropic

## Package Structure

- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted code snippets and usage samples

## Mini-Skills Index

### ad-creative
- Summary: Generate high-performing ad copy at scale — headlines, descriptions, and primary text with character-count validation and iteration tracking.
- Open reference: `references/skills/ad-creative.md`
- Open examples: `examples/skills/ad-creative.md`

### brand-bible
- Summary: Write user-facing copy following brand voice guidelines covering tone, personality, conciseness, and context-appropriate writing.
- Open reference: `references/skills/brand-bible.md`
- Open examples: `examples/skills/brand-bible.md`

### brand-guidelines-anthropic
- Summary: Apply Anthropic's official brand identity including colors, typography (Poppins/Lora), and visual formatting to artifacts and documents.
- Open reference: `references/skills/brand-guidelines-anthropic.md`
- Open examples: `examples/skills/brand-guidelines-anthropic.md`

### brand-guidelines-community
- Summary: Apply community-edition brand guidelines with Anthropic-aligned colors, typography (Poppins/Lora), and visual identity for community projects.
- Open reference: `references/skills/brand-guidelines-community.md`
- Open examples: `examples/skills/brand-guidelines-community.md`

### canvas-design
- Summary: Create design philosophies as aesthetic movements and express them visually on canvas, producing .md philosophy documents and .pdf or .png visual artifacts.
- Open reference: `references/skills/canvas-design.md`
- Open examples: `examples/skills/canvas-design.md`

### design-md
- Summary: Create DESIGN.md files as design system documentation for Stitch projects, capturing visual themes, color palettes, typography, component styles, and layout principles.
- Open reference: `references/skills/design-md.md`
- Open examples: `examples/skills/design-md.md`

### design-orchestration
- Summary: Control the flow between design skills — ensuring ideas become designs, designs are reviewed, and only validated designs reach implementation.
- Open reference: `references/skills/design-orchestration.md`
- Open examples: `examples/skills/design-orchestration.md`

### theme-factory
- Summary: Apply consistent, professional themes with cohesive color palettes and font pairings to slide decks and artifacts from 10 pre-built themes.
- Open reference: `references/skills/theme-factory.md`
- Open examples: `examples/skills/theme-factory.md`

### web-design-codex
- Summary: Review web interface files for compliance with Vercel's Web Interface Guidelines, outputting findings in terse file:line format.
- Open reference: `references/skills/web-design-codex.md`
- Open examples: `examples/skills/web-design-codex.md`

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
