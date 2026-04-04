---
name: "pretext-architecture-review"
title: "Architecture Review"
description: "Use for repo review, contributor audits, change-risk reviews, and system-level decision quality assessment."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/architecture-review.md`
- Examples: `examples/skills/architecture-review.md`
- Anti-patterns: `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/ANTI-PATTERNS.md` — Pretext anti-patterns
- Original docs: `original-docs/` — preserved original contributor documentation

# Architecture Review

## Purpose
Use this skill for repo review, contributor audits, change-risk reviews, and system-level decision quality.

## Review checklist
- Is the proposed change touching the hot `layout()` path unnecessarily?
- Is a browser-specific miss being overfit?
- Does the change preserve the separation between public API docs and internal notes?
- Are status claims backed by current snapshots?
- Are demos proving real API needs instead of ornamental wants?
- Is the packaging surface still coherent?
- Does the change respect the current roadmap and do-not-do guidance?

## Risk categories
- correctness risk
- browser-divergence risk
- benchmark regression risk
- retained-memory risk
- API surface risk
- corpus-overfitting risk
- release-shape risk

## Deliverable shape
A good review should state:
- what changed
- what subsystem it affects
- what evidence was checked
- what snapshots or dashboards must be refreshed
- what risks remain open
