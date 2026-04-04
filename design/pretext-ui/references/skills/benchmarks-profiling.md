---
name: "pretext-benchmarks-profiling"
title: "Benchmarks & Profiling"
description: "Use for hot-path performance work, benchmark regressions, CPU profiling, allocation churn, and retained-memory checks."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/benchmarks-profiling.md`
- Examples: `examples/skills/benchmarks-profiling.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Benchmarks & Profiling

## Purpose
Use this skill for hot-path performance work, benchmark regressions, CPU profiling, allocation churn, and retained-memory checks.

## Commands
```sh
bun run benchmark-check
bun run benchmark-check:safari
bun run status-dashboard
```

## Preferred profiling loop
1. Start `bun start`.
2. Launch an isolated Chrome with remote debugging and a throwaway profile.
3. Use a tiny dedicated repro page before the full benchmark page.
4. Ask the questions in order:
   - Is this a benchmark regression?
   - Where is CPU time going?
   - Is this allocation churn?
   - Is anything retained after GC?

## Tool choice
- Throughput/regression: benchmark page or a narrow stress page
- CPU hotspots: Chrome CPU profiler / performance trace
- Allocation churn: Chrome heap sampling during workload
- Retained memory: before/after heap snapshots with forced GC

## Performance doctrine
- `layout()` remains the resize hot path.
- `prepare()` is where script-specific cost lives.
- Keep the hot path simple and allocation-light.
- Use split `analyze()` / `measure()` benchmark rows to steer `prepare()` work.
- Use chunk-heavy rich benchmark rows to steer `layoutNextLine()` work.

## Refresh rules
Refresh `benchmarks/chrome.json` and `benchmarks/safari.json` when methodology or the hot path changes.
Then regenerate `status/dashboard.json`.
