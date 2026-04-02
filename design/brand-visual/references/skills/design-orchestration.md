---
name: "design-orchestration"
title: "Design Orchestration"
description: "Use for controlling the flow between design skills — ensuring ideas become designs, designs are reviewed, and only validated designs reach implementation."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure
- Main router: `SKILL.md`
- This reference: `references/skills/design-orchestration.md`
- Examples: `examples/skills/design-orchestration.md`

## Linked Package Files
- Adjacent: `references/skills/design-md.md` — for design documentation step
- Adjacent: `references/skills/web-design-codex.md` — for compliance review step
- Validation: `references/skills/canvas-design.md` — for visual creation step

## Purpose
Ensure that ideas become designs, designs are reviewed, and only validated designs reach implementation. This skill does not generate designs — it controls the flow between other design skills.

## When to Use
- When managing a multi-step design workflow
- When coordinating between ideation, creation, review, and implementation phases
- When ensuring design quality gates are not bypassed

## Workflow
1. Ideation: define design requirements and constraints.
2. Creation: route to the appropriate design skill (canvas-design, design-md, theme-factory).
3. Review: validate output against brand guidelines, web interface standards, and accessibility.
4. Approval: confirm the design meets all criteria before implementation.
5. Handoff: deliver validated design to implementation.

## Quality Standards
- No design should reach implementation without review.
- Every design must be validated against brand guidelines.
- The orchestration flow must be documented and traceable.

## Technical Rules
- Route ideation to the appropriate creation skill based on output type.
- Route review to web-design-codex and/or brand-guidelines as appropriate.
- Maintain a log of design decisions and review outcomes.

## Validation
- Confirm all design phases were executed in order.
- Verify review was completed before implementation handoff.
- Check that design decisions are documented.

## Restrictions
- Do not skip the review phase.
- Do not generate designs directly — delegate to specialized skills.

## Output Requirements
- Design workflow documentation with phase transitions.
- Review outcomes and approval status.
