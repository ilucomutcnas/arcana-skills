# Skill Catalog

This file maps each mini-skill to its reference and examples file.

## 1. ad-creative
- Summary: Generate high-performing ad copy at scale with platform-specific specs, angle-based organization, character-count validation, and performance-driven iteration.
- Reference: `references/skills/ad-creative.md`
- Examples: `examples/skills/ad-creative.md`

## 2. content-creator
- Summary: Create brand-consistent content with voice analysis, SEO-optimized blog posts, platform-specific social media content, and content calendar planning.
- Reference: `references/skills/content-creator.md`
- Examples: `examples/skills/content-creator.md`

## 3. pdf-processing
- Summary: Process PDF documents programmatically using Python and CLI tools for merging, splitting, extraction, form filling, OCR, and creation.
- Reference: `references/skills/pdf-processing.md`
- Examples: `examples/skills/pdf-processing.md`

## 4. vector-workflow-automation
- Summary: Normalize vector assets and automate SVG hygiene, naming standards, complexity control, token-aware styling, and export planning for design systems.
- When to use: Icon cleanup, mixed-source SVG normalization, and engineering-ready vector package preparation.
- Related: Pairs with `creative-asset-handoff` for implementation delivery and with `ad-creative` for campaign visual consistency.
- Reference: `references/skills/vector-workflow-automation.md`
- Examples: `examples/skills/vector-workflow-automation.md`

## 5. raster-retouch-pipeline
- Summary: Run non-destructive image retouch workflows with source preservation, channel-specific crops, profile-aware exports, and QA gates.
- When to use: Product/photo cleanup, campaign visual optimization, and multi-channel raster exports.
- Related: Pairs with `ad-creative` for final campaign visuals and with `creative-asset-handoff` for packaging approved variants.
- Reference: `references/skills/raster-retouch-pipeline.md`
- Examples: `examples/skills/raster-retouch-pipeline.md`

## 6. creative-asset-handoff
- Summary: Deliver complete creative asset packages with deterministic naming, source/export separation, manifesting, provenance notes, and acceptance criteria.
- When to use: Final delivery to engineering, marketing, clients, or operations with audit-friendly packaging.
- Related: Connects all production mini-skills (`vector-workflow-automation`, `raster-retouch-pipeline`, `pdf-processing`, `content-creator`) into release-ready output.
- Reference: `references/skills/creative-asset-handoff.md`
- Examples: `examples/skills/creative-asset-handoff.md`

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
