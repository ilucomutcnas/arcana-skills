---
name: "css-language-conventions"
title: "CSS Naming & Language Conventions"
description: "Rules for CSS naming, comments, mixed-language teams, and multilingual codebases."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/language-conventions.md`
- Examples: `examples/skills/language-conventions.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — universal CSS guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — CSS anti-patterns reference

# CSS Naming & Language Conventions

## Purpose
Keep CSS understandable in multilingual or mixed-discipline teams.

## Naming doctrine

- Prefer English for class names, custom properties, file names, and public styling APIs unless the project has an explicit alternative standard.
- Keep names descriptive but compact.
- Prefer domain meaning over appearance-only naming when the class is reusable.
- Use appearance naming only for tightly local layout helpers.

## Comment doctrine

Comments should explain:
- why a strange workaround exists
- browser constraints
- token rationale
- temporary migration boundaries
- interaction or motion intent

Comments should not narrate obvious CSS.

## Mixed-language content rules

If the team writes product copy in multiple languages:
- keep class names language-neutral
- keep tokens language-neutral
- keep comments in one primary engineering language
- avoid transliterated chaos in selectors and filenames

## Good practices

- `product-card`, `site-header`, `form-section`, `--color-accent`
- one language for engineering comments
- glossary for domain-specific naming

## Bad practices

- `final-2`
- mixing English, Russian, and local transliteration in class names
- comments that only restate the property below them
