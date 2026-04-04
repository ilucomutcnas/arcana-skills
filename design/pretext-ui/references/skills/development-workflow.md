---
name: "pretext-development-workflow"
title: "Development Workflow"
description: "Use for setup, command selection, local iteration, page navigation, and the standard Pretext contributor loop."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/development-workflow.md`
- Examples: `examples/skills/development-workflow.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Development Workflow

## Purpose
Use this skill for setup, command selection, local iteration, and the normal contributor loop.

## Setup
```sh
bun install
bun start
```

## Core command surface
- `bun start` — stable demo pages
- `bun run start:lan` — LAN-reachable dev server
- `bun run start:watch` — watch/reload mode
- `bun run site:build` — static demo site build
- `bun run check` — typecheck and lint
- `bun test` — invariant suite
- `bun run build:package` — emit `dist/`
- `bun run package-smoke-test` — tarball verification

## Use these pages
- `/demos/index`
- `/demos/bubbles`
- `/demos/dynamic-layout`
- `/demos/editorial-engine`
- `/accuracy`
- `/benchmark`
- `/corpus`

## Current sources of truth
- `STATUS.md`
- `status/dashboard.json`
- `accuracy/*.json`
- `benchmarks/*.json`
- `corpora/STATUS.md`
- `corpora/dashboard.json`
- `corpora/representative.json`
- `RESEARCH.md`

## Workflow discipline
- Use the stable page server unless you explicitly need watch/reload.
- Prefer checked-in dashboards and snapshots before making status claims.
- Keep command lists synchronized with `DEVELOPMENT.md` instead of inventing parallel instructions.
