# Routing Guide

Use this guide to decide which extracted file to open.

## Rules

- Keep the main `SKILL.md` lightweight and navigational.
- Open `resources/skill-catalog.md` for the full index.
- Open `references/skills/<slug>.md` for the full methodology and validation rules.
- Open `examples/skills/<slug>.md` for sample code and usage patterns.
- If a task spans multiple domains, combine the relevant reference files.

## Quick Navigation

- **ad-creative** -> `references/skills/ad-creative.md` and `examples/skills/ad-creative.md`
- **content-creator** -> `references/skills/content-creator.md` and `examples/skills/content-creator.md`
- **pdf-processing** -> `references/skills/pdf-processing.md` and `examples/skills/pdf-processing.md`

## Routing by Task Type

- **Generating ad copy** -> ad-creative (primary) + content-creator (brand voice)
- **Iterating ads from data** -> ad-creative
- **Writing blog posts** -> content-creator (primary) + ad-creative (promotion copy)
- **Social media content** -> content-creator
- **Brand voice setup** -> content-creator
- **Content calendar** -> content-creator
- **Merging/splitting PDFs** -> pdf-processing
- **Extracting text/tables** -> pdf-processing
- **Filling PDF forms** -> pdf-processing
- **Creating PDFs** -> pdf-processing
- **Branded PDF documents** -> pdf-processing + content-creator

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
