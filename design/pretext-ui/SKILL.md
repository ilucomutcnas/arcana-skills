---
name: "pretext-ui"
title: "Pretext Contributor Mini Skills"
description: "Operational package for maintaining Pretext text layout: architecture, contributor workflow, browser accuracy, performance, corpus diagnostics, packaging, demos, roadmap governance, research continuity, and architecture review."
version: "1.0.0"
category: "Engineering"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide contributor-grade operating guidance for Pretext maintenance and upgrades. The package keeps the same 10 mini-skills and deepens execution quality for public API changes, browser parity, corpus-driven diagnostics, performance evidence, and release readiness.

## Domain Coverage

Covers Pretext engine internals (`analysis`, `measurement`, `line-break`, `bidi`, `layout`), browser accuracy sweeps, corpus probes across scripts, benchmark/profiling interpretation, package release confidence, demo dogfooding loops, roadmap governance, research memory, and system-level architecture review.

## How to Use

1. Run `self-diagnostic-protocol.md` before work.
2. Pick a **primary** mini-skill from `resources/skill-catalog.md`.
3. Add at least two adjacent mini-skills plus one validation mini-skill for non-trivial work.
4. Route through `resources/routing-guide.md` for scenario composition.
5. Open reference + example files for each activated mini-skill.

## Primary + Adjacent Validation Guidance

- **Public layout API or metadata change**: primary `library-architecture`; adjacent `browser-accuracy`, `corpus-diagnostics`; validation `architecture-review`.
- **Mismatch visible in demo/pages**: primary `browser-accuracy`; adjacent `library-architecture`, `corpus-diagnostics`; validation `benchmarks-profiling`.
- **Speed/memory regression**: primary `benchmarks-profiling`; adjacent `library-architecture`, `development-workflow`; validation `architecture-review`.
- **Release candidate confidence**: primary `packaging-release`; adjacent `demo-dogfooding`, `browser-accuracy`; validation `development-workflow`.

## Package Structure

- `SKILL.md` — concise router
- `composition-protocol.md` — universal composition + concrete recipes
- `self-diagnostic-protocol.md` — gate checks and rejection criteria
- `resources/skill-catalog.md` — all 10 mini-skills with use-with guidance
- `resources/routing-guide.md` — scenario routing matrix
- `resources/asset-link-index.md` — references/examples/resources index
- `resources/manifest.json` — machine-readable package map
- `references/skills/*.md` — operational doctrine
- `examples/skills/*.md` — end-to-end contributor scenarios
- `shared-rules/ANTI-PATTERNS.md` — package anti-patterns

## Mini-Skills

`library-architecture`, `development-workflow`, `browser-accuracy`, `benchmarks-profiling`, `corpus-diagnostics`, `packaging-release`, `demo-dogfooding`, `priorities-roadmap`, `research-log`, `architecture-review`.

## Non-Goals

- No replacement of existing package semantics.
- No unrelated repo-wide policy changes.
- No deletion of existing routing/index sections.
