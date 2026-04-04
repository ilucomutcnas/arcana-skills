---
name: "pretext-corpus-diagnostics"
title: "Corpus Diagnostics"
description: "Use for long-form corpus canaries, width sweeps, probes, extractor questions, font matrices, and mismatch taxonomy work."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/corpus-diagnostics.md`
- Examples: `examples/skills/corpus-diagnostics.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Corpus Diagnostics

## Purpose
Use this skill for long-form corpus canaries, width sweeps, probes, extractor questions, font matrices, and mismatch taxonomy work.

## Commands
```sh
bun run corpus-check
bun run corpus-sweep
bun run corpus-font-matrix
bun run corpus-taxonomy
bun run corpus-representative
bun run corpus-status
bun run corpus-status:refresh
bun run gatsby-check
bun run gatsby-sweep
```

## Corpus doctrine
- Sweep widths cheaply first.
- Diagnose only the mismatching widths in detail.
- Broaden canaries only when the source text is clean.
- Reject dirty or wrapped raw-source corpora that create false lessons.
- Use mixed app text as a first-class product-shaped canary.
- Prefer Chrome for the first font-matrix pass.

## Script-sensitive guidance
- Arabic/Urdu: use normalized slices, exact corpus font, and RTL range-based diagnostics.
- Southeast Asian and mixed Thai/Lao/Khmer/Myanmar text: prefer range-based corpus diagnostics over span probing.
- Safari URL/query probe misses should be cross-checked with `--method=span` before changing the engine.

## Representative keeps
- URL/query-string handling
- escaped quote clusters
- numeric/time-range runs
- emoji ZWJ runs
- explicit zero-width separators where source text is clean
- soft-hyphen canaries when the miss is truly product-shaped

## Refresh rules
Refresh corpus snapshots and dashboards when sweep methodology or long-form canary behavior changes in a way that moves the checked-in status.
