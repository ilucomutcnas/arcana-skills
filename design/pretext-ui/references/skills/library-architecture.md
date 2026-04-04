---
name: "pretext-library-architecture"
title: "Pretext Library Architecture"
description: "Use for core text-analysis, measurement, line-breaking, bidi metadata, and public layout API changes in the Pretext engine."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/library-architecture.md`
- Examples: `examples/skills/library-architecture.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Library Architecture

## Purpose
Use this skill when changing Pretext's core text-analysis, measurement, line-breaking, bidi metadata, or public layout APIs.

## Source of truth
- `README.md`
- `AGENTS.md`
- `src/layout.ts`
- `src/analysis.ts`
- `src/measurement.ts`
- `src/line-break.ts`
- `src/bidi.ts`

## Core doctrine
- `prepare()` / `prepareWithSegments()` do horizontal-only work.
- `layout()` / `layoutWithLines()` take explicit `lineHeight`.
- Keep `prepare()` as the opaque fast-path handle.
- Keep `layout()` fast, allocation-light, and free of DOM reads, canvas calls, and string work.
- Prefer preprocessing for script-specific break-policy fixes instead of pushing complexity into `layout()`.
- Preserve the richer internal segment model: normal text, collapsible spaces, preserved spaces, tabs, non-breaking glue, zero-width break opportunities, soft hyphens, and hard breaks.
- Keep bidi metadata on the rich path when `layout()` itself does not consume it.

## Public API guardrails
- Public examples and limitations should remain consistent with `README.md`.
- Do not re-expose internals on the main prepared type when `prepareWithSegments()` already covers richer needs.
- Keep manual layout helpers aligned with the rich path instead of contaminating the hot path.
- Treat `inline-flow` as a narrow sidecar, not a generic CSS inline formatting engine.

## Key architectural keeps
- Punctuation merges into preceding word-like segments, never into spaces.
- `NBSP`-style glue remains visible and prevents ordinary wrapping.
- `ZWSP` remains a zero-width break opportunity.
- Soft hyphen stays invisible when unbroken and surfaces a visible trailing hyphen when that break wins.
- Astral CJK and later extension blocks must keep hitting the CJK path.
- CJK grapheme splitting and kinsoku-style keeps must remain intact.

## Validation checklist
- Does the change preserve the fast `layout()` path?
- Does it belong in preprocessing instead of line layout?
- Does it widen the public API only when a real consumer proves the need?
- Does it preserve browser-facing behavior for `white-space: normal` and explicit `{ whiteSpace: 'pre-wrap' }` support?
