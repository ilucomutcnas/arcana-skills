---
name: "design-system-governance"
title: "Design System Governance"
description: "Defines contribution, review, versioning, deprecation, and ownership rules for sustainable design systems."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/governance.md`
- Examples: `examples/skills/governance.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Governance

## Purpose
Prevent system entropy.

## Governance areas
- ownership model
- decision records
- contribution workflow
- review criteria
- versioning
- deprecation
- adoption tracking

## Rules
1. Every token or component addition needs an explicit reason.
2. No new primitive without checking if an existing primitive already solves the problem.
3. Breaking changes must have migration notes.
4. Deprecations need timelines, alternatives, and communication.
5. Reviews must consider design, engineering, accessibility, and product impact.

## Suggested review gate
- What user/system problem does this solve?
- Why is the current system insufficient?
- Can this be solved by variant extension instead of a new component?
- What is the implementation cost?
- What is the long-term maintenance cost?
- What are the accessibility consequences?

## Versioning model
- patch: non-breaking fixes
- minor: additive improvements
- major: breaking contract changes

## Validation
- Can the system evolve without fragmenting?
- Are decisions traceable?
