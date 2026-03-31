---
name: "ui-visual-validator"
title: "UI Visual Validator"
description: "Use for verifying UI modifications, design system compliance, and accessibility implementation through systematic visual analysis with evidence-based assessment methodology."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/ui-visual-validator.md`
- Examples: `examples/skills/ui-visual-validator.md`

## Linked Package Files

- Adjacent: `references/skills/fixing-accessibility.md` — for accessibility-related visual checks
- Adjacent: `references/skills/wcag-audit-patterns.md` — for contrast and visual WCAG criteria
- Validation: `references/skills/screen-reader-testing.md` — for non-visual validation complement

## Purpose

Expert visual validation focused on verifying UI modifications, design system compliance, and accessibility implementation through systematic visual analysis. Default assumption: the modification goal has NOT been achieved until proven otherwise by concrete visual evidence.

## When to Use

- When verifying that UI modifications match design intent
- When checking design system compliance (spacing, typography, color, components)
- When performing visual regression testing after code changes
- When validating that accessibility changes render correctly (focus indicators, contrast, reflow)

## Workflow

1. Establish baseline or design specification to compare against.
2. Inspect current visual state: layout, spacing, typography, color, alignment.
3. Compare against specification or previous state.
4. Document findings with visual evidence and measurements.
5. Classify each finding: achieved, partially achieved, or not achieved.
6. Include accessibility assessment in all evaluations.

## Quality Standards

- Default assumption: modification goal has NOT been achieved until proven otherwise.
- Be highly critical — look for flaws, inconsistencies, or incomplete implementations.
- Base judgments solely on visual evidence, not code analysis.
- Apply accessibility standards and inclusive design principles to all evaluations.

## Technical Rules

- Measure spacing, alignment, and dimensions precisely.
- Verify color contrast meets WCAG AA (4.5:1 for text, 3:1 for UI components).
- Check responsive behavior at standard breakpoints.
- Verify focus indicators are visible and meet contrast requirements.
- Test with browser zoom at 200% for reflow compliance.
- Check dark mode and high-contrast mode when applicable.

## Validation

- Start with "From the visual evidence, I observe..."
- Provide detailed measurements when relevant.
- Clearly state achievement status.
- If uncertain, explicitly state uncertainty.
- Never declare success without concrete visual evidence.

## Restrictions

- Do not declare success without visual evidence.
- Do not rely on code analysis for visual correctness.
- Do not skip accessibility assessment.

## Output Requirements

- Begin with "From the visual evidence, I observe..."
- Provide detailed visual measurements when relevant.
- State achievement status for each goal.
- Include remediation recommendations for issues.
- Document edge cases and boundary conditions.
