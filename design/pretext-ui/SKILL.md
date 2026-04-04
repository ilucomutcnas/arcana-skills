---
name: "pretext-ui"
title: "Pretext Contributor Mini Skills"
description: "Use for working on the Pretext text-layout library: core engine work, browser-accuracy sweeps, corpus diagnostics, benchmarks, packaging, demos, architecture review, and contributor workflows. Covers line-breaking, bidi, measurement, script-sensitive analysis, and rich layout APIs."
version: "1.0.0"
category: "Engineering"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Purpose

Provide structured contributor guidance for the Pretext text-layout library. This domain covers core engine architecture, browser accuracy workflows, corpus diagnostics, performance profiling, packaging, demo dogfooding, roadmap priorities, research history, and architecture review — preserving the original task surface instead of deleting it.

## Domain Coverage

This package represents the Pretext library contributor domain. It covers the full contributor surface: engine internals (analysis, measurement, line-break, bidi, layout), cross-browser accuracy validation, multi-script corpus diagnostics, performance benchmarking, package publishing, demo-driven API dogfooding, roadmap governance, and architectural decision review.

Anti-patterns in `shared-rules/ANTI-PATTERNS.md` apply across all mini-skills. Original contributor documentation is preserved in `original-docs/`.

## How to Use

1. Always begin with self-diagnostic per `self-diagnostic-protocol.md`.
2. Identify the primary mini-skill that best matches the task.
3. Check the Multi-Skill Activation Guide below.
4. Open the corresponding reference under `references/skills/`.
5. Open examples under `examples/skills/` if routing guidance is needed.
6. Use `resources/skill-catalog.md` for the full index.
7. Use `resources/routing-guide.md` when a task spans multiple mini-skills.

## Multi-Skill Activation Guide

Common combinations:

- **Core engine change**: library-architecture (primary) + browser-accuracy + corpus-diagnostics + research-log
- **Browser sweep work**: browser-accuracy (primary) + corpus-diagnostics + benchmarks-profiling
- **Performance investigation**: benchmarks-profiling (primary) + library-architecture + browser-accuracy
- **Corpus expansion**: corpus-diagnostics (primary) + browser-accuracy + priorities-roadmap
- **Release preparation**: packaging-release (primary) + benchmarks-profiling + browser-accuracy + development-workflow
- **New demo**: demo-dogfooding (primary) + library-architecture + development-workflow
- **Contributor onboarding**: development-workflow (primary) + priorities-roadmap + architecture-review
- **Diff review**: architecture-review (primary) + library-architecture + research-log + priorities-roadmap

## Package Structure

- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted examples and routing patterns per mini-skill
- `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns reference
- `original-docs/` — preserved original contributor documentation
- `src/` — library source code
- `scripts/` — contributor automation scripts
- `pages/` — demo and diagnostic pages
- `corpora/` — multi-script text corpora for diagnostics
- `accuracy/` — browser accuracy snapshots
- `benchmarks/` — performance benchmark snapshots
- `research-data/` — research datasets

## Mini-Skills Index

### library-architecture
- Summary: Core engine work and API guardrails for analysis, measurement, line-breaking, bidi, and layout.
- Open reference: `references/skills/library-architecture.md`
- Open examples: `examples/skills/library-architecture.md`

### development-workflow
- Summary: Setup, commands, local iteration, and the standard contributor loop.
- Open reference: `references/skills/development-workflow.md`
- Open examples: `examples/skills/development-workflow.md`

### browser-accuracy
- Summary: Browser sweep work, accuracy claims, mismatch diagnosis, and snapshot refresh rules.
- Open reference: `references/skills/browser-accuracy.md`
- Open examples: `examples/skills/browser-accuracy.md`

### benchmarks-profiling
- Summary: Hot-path performance work, benchmark regressions, CPU profiling, allocation churn, and memory checks.
- Open reference: `references/skills/benchmarks-profiling.md`
- Open examples: `examples/skills/benchmarks-profiling.md`

### corpus-diagnostics
- Summary: Long-form corpus canaries, width sweeps, probes, font matrices, and script-sensitive mismatch taxonomy.
- Open reference: `references/skills/corpus-diagnostics.md`
- Open examples: `examples/skills/corpus-diagnostics.md`

### packaging-release
- Summary: Published package shape, dist output, entrypoints, build correctness, and release confidence checks.
- Open reference: `references/skills/packaging-release.md`
- Open examples: `examples/skills/packaging-release.md`

### demo-dogfooding
- Summary: Building and validating demos that exercise rich line APIs and editorial-layout capabilities.
- Open reference: `references/skills/demo-dogfooding.md`
- Open examples: `examples/skills/demo-dogfooding.md`

### priorities-roadmap
- Summary: Current priorities, active canaries, not-worth-doing guidance, and open design questions.
- Open reference: `references/skills/priorities-roadmap.md`
- Open examples: `examples/skills/priorities-roadmap.md`

### research-log
- Summary: Earlier experiments, rejected hypotheses, and durable conclusions that shape future work.
- Open reference: `references/skills/research-log.md`
- Open examples: `examples/skills/research-log.md`

### architecture-review
- Summary: Repo review, contributor audits, change-risk reviews, and system-level decision quality.
- Open reference: `references/skills/architecture-review.md`
- Open examples: `examples/skills/architecture-review.md`

## Non-Goals

- Do not rewrite the library into a different product.
- Do not silently drop current canaries, benchmarks, or status dashboards.
- Do not treat exploratory notes as public API commitments.

## Preservation Rule

When in doubt, preserve the repository's intent and reformat the guidance instead of deleting it.

## Validation

- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.

## Output Requirements

- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
