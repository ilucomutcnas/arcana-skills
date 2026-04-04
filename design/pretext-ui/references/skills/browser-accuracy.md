---
name: "pretext-browser-accuracy"
title: "Browser Accuracy"
description: "Use for browser sweep work, accuracy claims, mismatch diagnosis, and refresh rules for checked-in accuracy snapshots."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/browser-accuracy.md`
- Examples: `examples/skills/browser-accuracy.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Browser Accuracy

## Purpose
Use this skill for browser sweep work, accuracy claims, mismatch diagnosis, and refresh rules for checked-in accuracy snapshots.

## Commands
```sh
bun run accuracy-check
bun run accuracy-check:safari
bun run accuracy-check:firefox
bun run accuracy-snapshot
bun run accuracy-snapshot:safari
bun run accuracy-snapshot:firefox
bun run pre-wrap-check
```

## Accuracy doctrine
- Accuracy pages and checkers are expected to be green in all three installed browsers on fresh runs.
- Suspect stale tabs or stale servers before changing the algorithm.
- Keep browser-automation lock semantics intact.
- Keep the permanent `pre-wrap` coverage small and explicit.
- For default `white-space: normal`, prefer the normal diagnostic flow unless the whitespace mode itself is under test.

## Refresh rules
Refresh `accuracy/chrome.json`, `accuracy/safari.json`, and `accuracy/firefox.json` when a diff changes:
- browser sweep methodology
- `src/analysis.ts`
- `src/measurement.ts`
- `src/line-break.ts`
- `src/layout.ts`
- `src/bidi.ts`
- `pages/accuracy.ts`

## Claim hygiene
- Do not make broad accuracy claims from a stale page run.
- Do not patch the engine from one noisy extractor view alone.
- Treat the public accuracy page as a regression gate, not the only steering metric.
