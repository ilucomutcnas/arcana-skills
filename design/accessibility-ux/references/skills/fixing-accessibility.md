---
name: "fixing-accessibility"
title: "Fixing Accessibility"
description: "Use for reviewing and fixing UI accessibility violations with targeted, minimal patches covering ARIA attributes, semantic HTML, keyboard access, focus management, and form error linking."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/fixing-accessibility.md`
- Examples: `examples/skills/fixing-accessibility.md`

## Linked Package Files

- Adjacent: `references/skills/wcag-audit-patterns.md` — for WCAG criterion mapping
- Adjacent: `references/skills/screen-reader-testing.md` — for verifying fixes with assistive technology
- Validation: `references/skills/ui-visual-validator.md` — for confirming visual correctness of fixes

## Purpose

Apply targeted accessibility constraints to UI work. Review files against accessibility rules and report violations with exact line references, impact explanations, and concrete code-level fixes. Prefer minimal, scoped patches over large rewrites.

## When to Use

- When adding or changing buttons, links, inputs, menus, dialogs, tabs, dropdowns
- When building forms, validation, error states, helper text
- When implementing keyboard shortcuts or custom interactions
- When working on focus states, focus trapping, or modal behavior
- When rendering icon-only controls
- When adding hover-only interactions or hidden content

## Workflow

1. Review the file or component against the accessibility rules below.
2. For each violation found, report the exact line or snippet.
3. Explain why it matters in one short sentence.
4. Provide a concrete code-level fix.
5. Do not rewrite large parts of the UI — prefer minimal, targeted fixes.

## Quality Standards

- Every interactive element must be keyboard accessible.
- Every non-decorative image must have meaningful alt text.
- Every form input must have a programmatically associated label.
- Every error message must be linked to its field via `aria-describedby`.
- Every icon-only button must have `aria-label` and icons must have `aria-hidden="true"`.
- Every custom widget must expose correct role, state, and value to assistive technology.
- Focus must be managed correctly for modals, dialogs, and dynamic content.

## Technical Rules

- Use native HTML elements before reaching for ARIA (button, not div with role="button").
- All interactive elements must be reachable via Tab and operable via Enter/Space.
- Custom widgets must implement ARIA roles, states, and keyboard patterns from the WAI-ARIA Authoring Practices.
- Error states must set `aria-invalid="true"` and link messages with `aria-describedby`.
- Dynamic content updates must use `aria-live` regions.
- Decorative images must use `alt=""` and `aria-hidden="true"`.
- Color must never be the only means of conveying information.

## Validation

- Verify each fix resolves the specific violation without introducing new issues.
- Test keyboard navigation through the fixed component.
- Confirm screen reader announcements are correct after the fix.
- Check that focus management is preserved.

## Restrictions

- Do not rewrite large parts of the UI — apply minimal, targeted fixes.
- Do not remove existing accessibility features when fixing other issues.
- Do not use ARIA attributes when native HTML achieves the same result.
- Do not suppress focus outlines.

## Output Requirements

- List each violation with the exact line or snippet.
- Provide a one-sentence impact explanation for each.
- Provide a concrete code-level fix for each.
- Keep patches minimal and scoped.
