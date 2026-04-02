# Routing Guide

Use this guide to decide which extracted file to open.

## Rules

- Keep the main `SKILL.md` lightweight and navigational.
- Open `resources/skill-catalog.md` for the full index.
- Open `references/skills/<slug>.md` for the full methodology, guardrails, and validation rules.
- Open `examples/skills/<slug>.md` for sample commands, code, and usage patterns.
- If a task spans multiple domains, combine the relevant reference files instead of expanding the main `SKILL.md`.
- Always apply `shared-rules/STYLE-GUARDRAILS.md` across all writing tasks.

## Quick Navigation

### Copywriting and Editing
- **copywriting** → `references/skills/copywriting.md` and `examples/skills/copywriting.md`
- **copy-editing** → `references/skills/copy-editing.md` and `examples/skills/copy-editing.md`

### Professional Writing Disciplines
- **journalistic-writing** → `references/skills/journalistic-writing.md` and `examples/skills/journalistic-writing.md`
- **marketing-writing** → `references/skills/marketing-writing.md` and `examples/skills/marketing-writing.md`
- **business-writing** → `references/skills/business-writing.md` and `examples/skills/business-writing.md`
- **legal-writing** → `references/skills/legal-writing.md` and `examples/skills/legal-writing.md`

### Personal and Multilingual
- **general-writing** → `references/skills/general-writing.md` and `examples/skills/general-writing.md`
- **language-handling** → `references/skills/language-handling.md` and `examples/skills/language-handling.md`

## Routing by Task Type

- **New landing page copy** → copywriting + marketing-writing + copy-editing
- **Editing existing copy** → copy-editing + marketing-writing
- **News article or feature** → journalistic-writing + copy-editing + language-handling
- **Legal clause or policy** → legal-writing + business-writing + language-handling
- **Business email or memo** → business-writing + general-writing
- **Multilingual marketing** → marketing-writing + language-handling + copy-editing
- **Personal messages** → general-writing + language-handling
- **Product description** → marketing-writing + copy-editing
- **Executive summary** → business-writing + copy-editing

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
