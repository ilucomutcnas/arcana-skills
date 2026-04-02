# Routing Guide

Use this guide to decide which extracted file to open.

## Rules

- Keep the main `SKILL.md` lightweight and navigational.
- Open `resources/skill-catalog.md` for the full index.
- Open `references/skills/<slug>.md` for the full methodology, guardrails, and validation rules.
- Open `examples/skills/<slug>.md` for sample commands, code, and usage patterns.
- If a task spans multiple domains, combine the relevant reference files instead of expanding the main `SKILL.md`.

## Quick Navigation

### Creative and Copy
- **ad-creative** → `references/skills/ad-creative.md` and `examples/skills/ad-creative.md`
- **brand-bible** → `references/skills/brand-bible.md` and `examples/skills/brand-bible.md`

### Brand Identity
- **brand-guidelines-anthropic** → `references/skills/brand-guidelines-anthropic.md` and `examples/skills/brand-guidelines-anthropic.md`
- **brand-guidelines-community** → `references/skills/brand-guidelines-community.md` and `examples/skills/brand-guidelines-community.md`

### Visual Design
- **canvas-design** → `references/skills/canvas-design.md` and `examples/skills/canvas-design.md`
- **theme-factory** → `references/skills/theme-factory.md` and `examples/skills/theme-factory.md`

### Design Systems and Workflow
- **design-md** → `references/skills/design-md.md` and `examples/skills/design-md.md`
- **design-orchestration** → `references/skills/design-orchestration.md` and `examples/skills/design-orchestration.md`

### Review and Quality
- **web-design-codex** → `references/skills/web-design-codex.md` and `examples/skills/web-design-codex.md`

## Routing by Task Type

- **Writing ad copy** → ad-creative + brand-bible + brand-guidelines-anthropic
- **Applying brand styling** → brand-guidelines-anthropic or brand-guidelines-community + theme-factory
- **Creating visual art** → canvas-design + theme-factory
- **Documenting a design system** → design-md + brand-bible
- **Theming a slide deck** → theme-factory + brand-guidelines-anthropic
- **Multi-step design workflow** → design-orchestration + design-md + web-design-codex

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
