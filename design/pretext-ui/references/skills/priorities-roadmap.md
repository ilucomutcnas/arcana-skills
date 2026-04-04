---
name: "pretext-priorities-roadmap"
title: "Priorities & Roadmap"
description: "Use for deciding what to work on next, understanding active canaries, and knowing what not to reopen."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/priorities-roadmap.md`
- Examples: `examples/skills/priorities-roadmap.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Priorities & Roadmap

## Purpose
Use this skill when deciding what to work on next and what not to reopen.

## Current priorities
1. Keep the canaries honest.
2. Use split benchmark rows and chunk-heavy rich rows to steer engine work.
3. Keep demos as dogfood, not ornamental extras.

## Active canaries
- Mixed app text still matters.
- Chinese remains the clearest active CJK canary.
- Myanmar and Urdu remain shaping/context canaries but are not the main tuning target.

## Not worth doing right now
- Chasing universal exactness as the product claim.
- Putting measurement back in `layout()`.
- Resurrecting dirty corpora only to cover another language.
- Overfitting one-line misses in one browser/corpus without broader evidence.
- Turning browser-profile shims into a bag of ad hoc knobs.
- Exploding the public API with cache or engine knobs.

## Still-open design questions
- browser shim vs runtime calibration for line-fit tolerance
- broader `pre-wrap` support
- `system-ui` fallback strategy
- server canvas support
- automatic hyphenation scope
- intrinsic sizing / logical width APIs
- bidi rendering scope
- optional slow verify path
