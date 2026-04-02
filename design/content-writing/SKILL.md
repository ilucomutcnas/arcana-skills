---
name: "content-writing"
title: "Content & Writing Mastery"
description: "Use for professional writing across journalism, marketing, business, legal, and general communication. Covers copywriting, copy editing, multilingual handling, and style discipline. Produces clear, evidence-aware, audience-fit prose without AI tics."
version: "1.0.0"
category: "Writing"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Produce task-fit, audience-aware writing across multiple professional disciplines. This domain covers journalistic reporting, marketing conversion copy, business communication, legal drafting, everyday personal writing, multilingual handling, structured copywriting, and systematic copy editing — with shared style guardrails that prevent tone bleed and unsupported claims.

## Domain Coverage

This package represents the content writing domain. It covers multiple interconnected writing disciplines, each with distinct standards, structures, and tone requirements. Writing tasks rarely fit a single generic mode — a marketing landing page requires different discipline than a legal clause or a news lede. Mini-skills are separated so the agent can apply the right standards for the right medium.

Shared guardrails in `shared-rules/STYLE-GUARDRAILS.md` apply across all writing skills unless a specific skill overrides them.

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

- **Landing page from scratch**: copywriting (primary) + marketing-writing + copy-editing
- **Editing existing marketing copy**: copy-editing (primary) + marketing-writing + copywriting
- **News article**: journalistic-writing (primary) + copy-editing + language-handling
- **Legal clause or policy**: legal-writing (primary) + business-writing + language-handling
- **Business email or memo**: business-writing (primary) + general-writing + language-handling
- **Multilingual marketing**: marketing-writing (primary) + language-handling + copy-editing
- **Bilingual legal document**: legal-writing (primary) + language-handling + copy-editing
- **Casual personal message**: general-writing (primary) + language-handling

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
- `shared-rules/STYLE-GUARDRAILS.md` — cross-skill style discipline

## Mini-Skills Index

### copywriting
- Summary: Produce clear, credible, action-oriented marketing copy through a phased process of context gathering, brief lock, structured page writing, and testability guidance.
- Open reference: `references/skills/copywriting.md`
- Open examples: `examples/skills/copywriting.md`

### copy-editing
- Summary: Systematically improve existing copy through seven sequential editing sweeps covering clarity, voice, relevance, proof, specificity, emotion, and risk reduction.
- Open reference: `references/skills/copy-editing.md`
- Open examples: `examples/skills/copy-editing.md`

### journalistic-writing
- Summary: Produce newsroom-grade, evidence-aware writing with public-interest structure, attribution discipline, and controlled language for news, features, and explainers.
- Open reference: `references/skills/journalistic-writing.md`
- Open examples: `examples/skills/journalistic-writing.md`

### marketing-writing
- Summary: Produce persuasive, conversion-oriented writing tuned for audience, offer, and action across landing pages, ads, emails, and product copy.
- Open reference: `references/skills/marketing-writing.md`
- Open examples: `examples/skills/marketing-writing.md`

### business-writing
- Summary: Produce clear, efficient professional communication for email, chat, memos, status reports, proposals, and executive summaries.
- Open reference: `references/skills/business-writing.md`
- Open examples: `examples/skills/business-writing.md`

### legal-writing
- Summary: Produce legally cautious, structured drafting support for clauses, policies, notices, disclaimers, and formal documents with risk awareness.
- Open reference: `references/skills/legal-writing.md`
- Open examples: `examples/skills/legal-writing.md`

### general-writing
- Summary: Produce natural, emotionally appropriate everyday text for personal messages, social posts, casual notes, and informal communication.
- Open reference: `references/skills/general-writing.md`
- Open examples: `examples/skills/general-writing.md`

### language-handling
- Summary: Control multilingual input, translation fidelity, code-switching, and target-language consistency across all writing tasks.
- Open reference: `references/skills/language-handling.md`
- Open examples: `examples/skills/language-handling.md`

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
