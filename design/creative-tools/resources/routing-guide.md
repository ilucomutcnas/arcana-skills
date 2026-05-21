# Routing Guide

Use this guide to decide which extracted file to open.

## Rules

- Keep the main `SKILL.md` lightweight and navigational.
- Open `resources/skill-catalog.md` for the full index.
- Open `references/skills/SLUG.md` for the full methodology and validation rules.
- Open `examples/skills/SLUG.md` for sample workflows and output patterns.
- If a task spans multiple concerns, combine relevant mini-skills.

## Quick Navigation

- **creative-qa-gate-automation** -> `references/skills/creative-qa-gate-automation.md` + `examples/skills/creative-qa-gate-automation.md`
- **ad-creative** -> `references/skills/ad-creative.md` + `examples/skills/ad-creative.md`
- **content-creator** -> `references/skills/content-creator.md` + `examples/skills/content-creator.md`
- **pdf-processing** -> `references/skills/pdf-processing.md` + `examples/skills/pdf-processing.md`
- **vector-workflow-automation** -> `references/skills/vector-workflow-automation.md` + `examples/skills/vector-workflow-automation.md`
- **raster-retouch-pipeline** -> `references/skills/raster-retouch-pipeline.md` + `examples/skills/raster-retouch-pipeline.md`
- **creative-asset-handoff** -> `references/skills/creative-asset-handoff.md` + `examples/skills/creative-asset-handoff.md`

## Routing by Task Type

- **Creative QA gate** -> creative-qa-gate-automation (primary) + relevant production mini-skills
- **Campaign release signoff** -> creative-qa-gate-automation (primary) + creative-asset-handoff
- **Cross-channel deliverable validation** -> creative-qa-gate-automation + ad-creative + content-creator + vector-workflow-automation + raster-retouch-pipeline + pdf-processing
- **Ad copy compliance review** -> creative-qa-gate-automation + ad-creative
- **Content launch approval** -> creative-qa-gate-automation + content-creator
- **Icon system QA** -> creative-qa-gate-automation + vector-workflow-automation
- **Product image release QA** -> creative-qa-gate-automation + raster-retouch-pipeline
- **PDF delivery QA** -> creative-qa-gate-automation + pdf-processing
- **Late revision loop** -> creative-qa-gate-automation + owning mini-skill + creative-asset-handoff
- **Stakeholder approval matrix** -> creative-qa-gate-automation (primary)
- **Generating ad copy** -> ad-creative (primary) + content-creator (brand voice)
- **Iterating ads from data** -> ad-creative
- **Writing blog posts** -> content-creator (primary) + ad-creative (promotion copy)
- **Social media content** -> content-creator
- **Brand voice setup** -> content-creator
- **Content calendar** -> content-creator
- **Campaign visual production** -> raster-retouch-pipeline (primary) + ad-creative
- **Icon set cleanup and export** -> vector-workflow-automation (primary) + creative-asset-handoff
- **Product image cleanup** -> raster-retouch-pipeline
- **Merging/splitting PDFs** -> pdf-processing
- **Extracting text/tables** -> pdf-processing
- **Filling PDF forms** -> pdf-processing
- **Creating PDFs** -> pdf-processing
- **Branded PDF documents** -> pdf-processing + content-creator
- **Document delivery package** -> pdf-processing + creative-asset-handoff
- **Campaign package delivery** -> content-creator + creative-asset-handoff
- **Cross-channel release handoff** -> creative-asset-handoff (primary) + vector-workflow-automation + raster-retouch-pipeline

## Shared Rules

- Read `../shared-rules/STYLE-GUARDRAILS.md` before delivering cross-mini-skill work or package-level outputs.
- Read `../shared-rules/ANTI-PATTERNS.md` as a rejection checklist before final delivery.

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
