---
name: "creative-tools"
title: "Creative Tools Studio"
description: "Use for performance ad creative at scale (headlines, descriptions, platform-specific copy with iteration), content creation with brand voice analysis, SEO optimization, social media content, content calendar planning, vector workflow automation, raster retouch pipelines, creative asset handoff, and PDF processing (merge, split, extract, create, fill forms, OCR)."
version: "1.1.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide structured guidance for creative production tools: generating and iterating performance ad copy at scale, creating brand-consistent content with SEO optimization, automating vector and raster creative production, packaging creative asset handoff for cross-functional stakeholders, and processing PDF documents programmatically. This domain connects ad creative workflows, content marketing pipelines, visual production operations, and document automation into a coherent creative toolset.

## Domain Coverage

This package represents the creative tools domain. It covers six interconnected capabilities: performance ad creative generation with platform specs and iteration tracking, content creation with brand voice analysis and SEO optimization, PDF processing for document automation, vector workflow automation for SVG/icon normalization, raster retouch pipelines for non-destructive image production, and creative asset handoff for release-ready delivery. Mini-skills are separated for routing and selective loading while still supporting multi-skill composition.

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

- **Full ad campaign**: ad-creative (primary) + content-creator (for brand voice consistency) + raster-retouch-pipeline (for visual cleanup) + creative-asset-handoff (for final delivery)
- **Content marketing pipeline**: content-creator (primary) + ad-creative (for promotion copy) + creative-asset-handoff (for release package)
- **Brand launch content**: content-creator (primary) + ad-creative + raster-retouch-pipeline + pdf-processing (for branded PDFs)
- **Icon system release**: vector-workflow-automation (primary) + creative-asset-handoff (for engineering and design-system delivery)
- **Document automation**: pdf-processing (primary) + content-creator (for document content) + creative-asset-handoff (for distribution readiness)

## Package Structure

- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `shared-rules/STYLE-GUARDRAILS.md` — package-wide output guardrails used across mini-skills
- `shared-rules/ANTI-PATTERNS.md` — package-wide mistakes and rejection checks used across mini-skills
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

### vector-workflow-automation
- Summary: Guide automated and semi-automated vector production workflows including SVG cleanup, icon normalization, path simplification, token-aware outputs, batch export planning, and design-system-ready QA.
- Open reference: `references/skills/vector-workflow-automation.md`
- Open examples: `examples/skills/vector-workflow-automation.md`

### raster-retouch-pipeline
- Summary: Run non-destructive raster retouch operations for cleanup, correction, crop/resize variants, profile-aware exports, and review gates across web/social/product channels.
- Open reference: `references/skills/raster-retouch-pipeline.md`
- Open examples: `examples/skills/raster-retouch-pipeline.md`

### creative-asset-handoff
- Summary: Package final creative deliverables with deterministic naming, source/export separation, versioning, provenance notes, stakeholder usage instructions, and acceptance criteria.
- Open reference: `references/skills/creative-asset-handoff.md`
- Open examples: `examples/skills/creative-asset-handoff.md`

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
