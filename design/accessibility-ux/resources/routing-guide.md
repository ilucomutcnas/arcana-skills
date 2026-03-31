# Routing Guide

Use this guide to decide which extracted file to open.

## Rules

- Keep the main `SKILL.md` lightweight and navigational.
- Open `resources/skill-catalog.md` for the full index.
- Open `references/skills/<slug>.md` for the full methodology, guardrails, and validation rules.
- Open `examples/skills/<slug>.md` for sample commands, code, and usage patterns.
- If a task spans multiple domains, combine the relevant reference files instead of expanding the main `SKILL.md`.

## Quick Navigation

### Fixing and Remediation
- **fixing-accessibility** → `references/skills/fixing-accessibility.md` and `examples/skills/fixing-accessibility.md`
- **fixing-metadata** → `references/skills/fixing-metadata.md` and `examples/skills/fixing-metadata.md`
- **fixing-motion-performance** → `references/skills/fixing-motion-performance.md` and `examples/skills/fixing-motion-performance.md`

### Testing and Validation
- **screen-reader-testing** → `references/skills/screen-reader-testing.md` and `examples/skills/screen-reader-testing.md`
- **ui-visual-validator** → `references/skills/ui-visual-validator.md` and `examples/skills/ui-visual-validator.md`

### Compliance and Auditing
- **wcag-audit-patterns** → `references/skills/wcag-audit-patterns.md` and `examples/skills/wcag-audit-patterns.md`

## Routing by Task Type

- **Reviewing a file for accessibility issues** → fixing-accessibility (primary) + wcag-audit-patterns + screen-reader-testing
- **Running a full WCAG audit** → wcag-audit-patterns (primary) + screen-reader-testing + fixing-accessibility + ui-visual-validator
- **Testing with screen readers** → screen-reader-testing (primary) + fixing-accessibility + wcag-audit-patterns
- **Verifying visual changes** → ui-visual-validator (primary) + fixing-accessibility + wcag-audit-patterns
- **Fixing animation jank** → fixing-motion-performance (primary) + fixing-accessibility + ui-visual-validator
- **Auditing page metadata/SEO** → fixing-metadata (primary) + ui-visual-validator
- **Building accessible components** → fixing-accessibility (primary) + wcag-audit-patterns + screen-reader-testing

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
