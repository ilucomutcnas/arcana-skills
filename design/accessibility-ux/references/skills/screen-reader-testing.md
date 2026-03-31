---
name: "screen-reader-testing"
title: "Screen Reader Testing"
description: "Use for testing web applications with screen readers (VoiceOver, NVDA, JAWS, TalkBack) covering navigation, forms, dynamic content, modals, live regions, and tab interfaces."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/screen-reader-testing.md`
- Examples: `examples/skills/screen-reader-testing.md`
- Implementation playbook: `screen-reader-testing__resources/implementation-playbook.md`

## Linked Package Files

- Adjacent: `references/skills/fixing-accessibility.md` — for fixing issues found during testing
- Adjacent: `references/skills/wcag-audit-patterns.md` — for mapping findings to WCAG criteria
- Validation: `references/skills/ui-visual-validator.md` — for verifying visual state during SR testing

## Purpose

Practical guide to testing web applications with screen readers for comprehensive accessibility validation. Covers the four major screen readers (VoiceOver, NVDA, JAWS, TalkBack), their commands, testing checklists, and common test scenarios including modals, live regions, tab interfaces, and form flows.

For detailed commands, checklists, and code patterns, see `screen-reader-testing__resources/implementation-playbook.md`.

## When to Use

- When validating screen reader compatibility
- When testing ARIA implementations
- When debugging assistive technology issues
- When verifying form accessibility
- When testing dynamic content announcements
- When ensuring navigation accessibility

## Workflow

1. Choose screen reader and browser combination based on testing priority.
2. Test page load: title announced, main landmark found, skip link works.
3. Test navigation: headings via rotor, heading levels logical, landmarks labeled.
4. Test interactive elements: links, buttons, forms, custom widgets.
5. Test dynamic content: alerts, loading states, content updates, modals.
6. Document findings and map to WCAG criteria.

Minimum coverage: NVDA + Firefox (Windows), VoiceOver + Safari (macOS), VoiceOver + Safari (iOS).

## Quality Standards

- Test with actual screen readers, not simulators.
- Use semantic HTML first — ARIA is supplemental.
- Test in both browse and focus modes.
- Verify focus management, especially for SPAs.
- Test keyboard-only navigation first as foundation.

## Technical Rules

- VoiceOver modifier: Ctrl + Option. Key commands: VO+Right/Left (navigate), VO+Space (activate), VO+U (rotor).
- NVDA modifier: Insert. Key commands: H (headings), F (form fields), D (landmarks), NVDA+F7 (elements list).
- JAWS quick keys: H (heading), T (table), F (form field), ; (landmark).
- TalkBack gestures: swipe right/left (navigate), double tap (activate).

## Validation

- Confirm all content announced in logical reading order.
- Verify interactive elements announce role, name, and state.
- Check dynamic content changes announced via live regions.
- Test focus trapping in modals and return on close.

## Restrictions

- Do not rely on a single screen reader — test at least two.
- Do not ignore mobile screen readers.
- Do not test only the happy path — include error states.

## Output Requirements

- Document each finding with steps to reproduce.
- Map findings to WCAG criteria.
- Provide remediation recommendations.
