---
name: "pretext-demo-dogfooding"
title: "Demo Dogfooding"
description: "Use for building, updating, or validating demos that exercise the rich line APIs and editorial-layout capabilities."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/demo-dogfooding.md`
- Examples: `examples/skills/demo-dogfooding.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Demo Dogfooding

## Purpose
Use this skill when building, updating, or validating demos that exercise the rich line APIs and editorial-layout capabilities.

## Demo doctrine
- Keep editorial demos as the dogfood path for rich line APIs.
- Prefer `layoutNextLine()` and `walkLineRanges()` when the demo is about streaming or obstacle-aware layout.
- Add a new demo only if it exposes something current editorial demos do not already cover.
- Let browser demos increasingly dogfood `layoutNextLine()` instead of relying only on whole-paragraph materialization.

## Current useful pages
- `/demos/bubbles`
- `/demos/dynamic-layout`
- `/demos/editorial-engine`
- `/demos/justification-comparison`
- `/demos/markdown-chat`

## Expansion rule
If a future custom-layout page wants more metadata, prove the need there before expanding the public rich API.
