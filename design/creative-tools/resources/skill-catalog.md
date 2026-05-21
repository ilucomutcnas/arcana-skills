# Skill Catalog

This file maps each mini-skill to its reference and examples file.

## 1. ad-creative
- Summary: Generate high-performing ad copy at scale with platform-specific specs, angle-based organization, character-count validation, and performance-driven iteration.
- Use with: `creative-qa-gate-automation` for compliant ad variation release and evidence-backed signoff.
- Reference: `references/skills/ad-creative.md`
- Examples: `examples/skills/ad-creative.md`

## 2. content-creator
- Summary: Create brand-consistent content with voice analysis, SEO-optimized blog posts, platform-specific social media content, and content calendar planning.
- Use with: `creative-qa-gate-automation` for editorial launch approval and stakeholder signoff.
- Reference: `references/skills/content-creator.md`
- Examples: `examples/skills/content-creator.md`

## 3. pdf-processing
- Summary: Process PDF documents programmatically using Python and CLI tools for merging, splitting, extraction, form filling, OCR, and creation.
- Use with: `creative-qa-gate-automation` + `creative-asset-handoff` for document delivery gates.
- Reference: `references/skills/pdf-processing.md`
- Examples: `examples/skills/pdf-processing.md`

## 4. vector-workflow-automation
- Summary: Normalize vector assets and automate SVG hygiene, naming standards, complexity control, token-aware styling, and export planning for design systems.
- Use with: `creative-qa-gate-automation` + `creative-asset-handoff` for icon release.
- Reference: `references/skills/vector-workflow-automation.md`
- Examples: `examples/skills/vector-workflow-automation.md`

## 5. raster-retouch-pipeline
- Summary: Run non-destructive image retouch workflows with source preservation, channel-specific crops, profile-aware exports, and QA gates.
- Use with: `creative-qa-gate-automation` for image variant signoff before release packaging.
- Reference: `references/skills/raster-retouch-pipeline.md`
- Examples: `examples/skills/raster-retouch-pipeline.md`

## 6. creative-asset-handoff
- Summary: Deliver complete creative asset packages with deterministic naming, source/export separation, manifesting, provenance notes, acceptance criteria, and rollback clarity.
- Use with: all production mini-skills after QA gate approval.
- Reference: `references/skills/creative-asset-handoff.md`
- Examples: `examples/skills/creative-asset-handoff.md`

## 7. creative-qa-gate-automation
- Summary: Coordinate review automation, validation matrices, severity triage, signoff workflows, revision loops, and release blocker decisions before final handoff.
- Use with: all six existing mini-skills for campaign release governance.
- Reference: `references/skills/creative-qa-gate-automation.md`
- Examples: `examples/skills/creative-qa-gate-automation.md`

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
