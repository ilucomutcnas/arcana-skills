# documentation Example

## Scenario: Button documentation page revamp for design-system portal

## Documentation Page Outline
1. Purpose and when to use
2. Anatomy diagram and slot definitions
3. Variants (`solid`, `outline`, `ghost`) and supported tones
4. States (default/hover/focus/disabled/loading)
5. Accessibility guidance (labels, focus, keyboard, motion)
6. Content guidance (action-first labels, destructive wording)
7. Examples (form submit, modal actions, toolbar compact actions)
8. Anti-patterns (multiple primary actions, icon-only without label)
9. Implementation notes (React props, CSS vars, Tailwind mapping)

## Migration Note
Legacy `PrimaryCta` and `SecondaryCta` components are deprecated. Map to `Button variant="solid"` and `Button variant="outline"` by release `v4.2`.

## Adoption Note
Teams must link to this page in PR templates when introducing new button usage. Design reviews require screenshot references to documented states.
