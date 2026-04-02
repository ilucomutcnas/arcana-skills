---
name: "creative-tools"
title: "Creative Tools Studio"
description: "Use for performance ad creative at scale (headlines, descriptions, platform-specific copy with iteration), content creation with brand voice analysis, SEO optimization, social media content, content calendar planning, and PDF processing (merge, split, extract, create, fill forms, OCR)."
version: "1.0.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide structured guidance for creative production tools: generating and iterating performance ad copy at scale, creating brand-consistent content with SEO optimization, and processing PDF documents programmatically. This domain connects ad creative workflows, content marketing pipelines, and document automation into a coherent creative toolset.

## Domain Coverage

This package represents the creative tools domain. It covers three interconnected capabilities: performance ad creative generation with platform specs and iteration tracking, content creation with brand voice analysis and SEO optimization, and PDF processing for document automation. Mini-skills are separated for routing and selective loading — ad copy production and content creation share references and often feed into each other.

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

- **Full ad campaign**: ad-creative (primary) + content-creator (for brand voice consistency)
- **Content marketing pipeline**: content-creator (primary) + ad-creative (for promotion copy)
- **Brand launch content**: content-creator (primary) + ad-creative + pdf-processing (for branded PDFs)
- **Document automation**: pdf-processing (primary) + content-creator (for document content)

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
- Summary: Generate high-performing ad copy at scale with platform-specific specs, angle-based organization, character-count validation, AI+Remotion visual workflows, and performance-driven iteration.
- Open reference: `references/skills/ad-creative.md`
- Open examples: `examples/skills/ad-creative.md`

### content-creator
- Summary: Create brand-consistent content with voice analysis, SEO-optimized blog posts, platform-specific social media content, and content calendar planning using scripts and reference frameworks.
- Open reference: `references/skills/content-creator.md`
- Open examples: `examples/skills/content-creator.md`

### pdf-processing
- Summary: Process PDF documents programmatically using Python (pypdf, pdfplumber, reportlab) and CLI tools (qpdf, pdftk) for merging, splitting, text extraction, table extraction, form filling, OCR, and creation.
- Open reference: `references/skills/pdf-processing.md`
- Open examples: `examples/skills/pdf-processing.md`

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
