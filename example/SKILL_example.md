---
name: "[name]"
title: "[title]"
description: "[description]"
version: "1.0.0"
category: "[category]"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose
[purpose]

## How to Use
1. Always begin with self-diagnostic. Start with a quick package integrity check, then validate only the activated working set. The self-diagnostic rules for this domain package are defined in `self-diagnostic-protocol.md`.
2. Identify the primary mini-skill that best matches the task.
3. Check the `Multi-Skill Activation Guide` below to load adjacent mini-skills that commonly co-occur with the primary task.
4. Open the corresponding reference file under `references/skills/`.
5. Open the corresponding examples file under `examples/skills/` if concrete commands, prompts, or code are needed.
6. Use `resources/skill-catalog.md` for the full index.
7. Use `resources/routing-guide.md` when a task spans multiple mini-skills.
8. Use `resources/asset-link-index.md` to find every auxiliary folder and file (all package assets, scripts, templates, and supporting materials).

## Multi-Skill Activation Guide
- Do not treat mini-skills as isolated when the task spans multiple concerns. Do not use a mini-skill in isolation unless the task is clearly narrow and self-contained. 
- Use combinations of mini-skills when the task involves architecture, implementation, evaluation, deployment, or adjacent domains.
- For all non-trivial tasks, apply the universal composition rule in `composition-protocol.md`.

## Package Structure
- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted code snippets, command examples, prompt patterns, and usage samples

## Mini-Skills Index

### [first-skill-name]
- Summary: [summary description]
- Open reference: `references/skills/[file-name].md`
- Open examples: `examples/skills/[file-name].md`

### [second-skill-name]
- Summary: [summary description]
- Open reference: `references/skills/[file-name].md`
- Open examples: `examples/skills/[file-name].md`

## Validation
- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.

## Output Requirements
- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
