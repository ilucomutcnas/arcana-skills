---
name: "design-system-documentation"
title: "Design System Documentation"
description: "Documents system intent, usage rules, component contracts, and adoption guidance for design and engineering teams."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/documentation.md`
- Examples: `examples/skills/documentation.md`
- Shared rules: `shared-rules/STYLE-GUARDRAILS.md`, `shared-rules/ANTI-PATTERNS.md`

## Linked Package Files

- Shared: `shared-rules/STYLE-GUARDRAILS.md` — design system style guardrails
- Shared: `shared-rules/ANTI-PATTERNS.md` — design system anti-patterns

# Design System Documentation

## Purpose
Make the system understandable, searchable, teachable, and adoptable.

## Documentation layers
- Foundations docs
- Component docs
- Content guidance
- Accessibility notes
- Theming notes
- Contribution rules
- Migration notes
- Release notes

## Rules
1. Explain **when to use** and **when not to use**.
2. Show code and design examples side by side when possible.
3. Document edge cases, not just happy paths.
4. Keep docs opinionated enough to prevent drift.
5. Write for mixed audiences: designers, engineers, reviewers, product teams.

## Minimum doc block for a component
- Purpose
- Anatomy
- Variants
- States
- Accessibility
- Content guidance
- Examples
- Anti-patterns
- Implementation notes

## Validation
- Could a new team adopt the component correctly without asking the original author for help?
