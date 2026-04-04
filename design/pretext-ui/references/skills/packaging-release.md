---
name: "pretext-packaging-release"
title: "Packaging & Release"
description: "Use for published package shape, dist output, entrypoints, build correctness, and release confidence checks."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/packaging-release.md`
- Examples: `examples/skills/packaging-release.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Packaging & Release

## Purpose
Use this skill for published package shape, dist output, entrypoints, build correctness, and release confidence checks.

## Important files
- `package.json`
- `tsconfig.build.json`
- `scripts/package-smoke-test.ts`

## Doctrine
- Published package ships built ESM from `dist/`.
- `dist/` is publish-time output, not checked-in source.
- Keep library-internal imports runtime-honest with `.js` specifiers inside `.ts` files.
- Use `bun run package-smoke-test` as the quickest published-artifact confidence check before release.

## Standard flow
```sh
bun run check
bun test
bun run build:package
bun run package-smoke-test
```

## Release caution
Do not change the export surface without verifying emitted files and smoke-test consumers.
