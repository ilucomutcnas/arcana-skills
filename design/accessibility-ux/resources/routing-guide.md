# Routing Guide

## Rules

- Keep the main `SKILL.md` lightweight and navigational.
- Open `resources/skill-catalog.md` for the full index.
- Open `references/skills/<slug>.md` for methodology, guardrails, and validation rules.
- Open `examples/skills/<slug>.md` for real execution patterns and deliverable formats.
- For multi-domain tasks, compose mini-skills; do not collapse workflows into a single generic route.

## Quick Navigation

### Fixing and Remediation
- **fixing-accessibility** → `references/skills/fixing-accessibility.md` and `examples/skills/fixing-accessibility.md`
- **fixing-metadata** → `references/skills/fixing-metadata.md` and `examples/skills/fixing-metadata.md`
- **fixing-motion-performance** → `references/skills/fixing-motion-performance.md` and `examples/skills/fixing-motion-performance.md`

### Testing and Validation
- **screen-reader-testing** → `references/skills/screen-reader-testing.md` and `examples/skills/screen-reader-testing.md`
- **assistive-tech-edge-cases** → `references/skills/assistive-tech-edge-cases.md` and `examples/skills/assistive-tech-edge-cases.md`
- **ui-visual-validator** → `references/skills/ui-visual-validator.md` and `examples/skills/ui-visual-validator.md`

### Compliance and Auditing
- **wcag-audit-patterns** → `references/skills/wcag-audit-patterns.md` and `examples/skills/wcag-audit-patterns.md`
- **wcag-audit-reporting** → `references/skills/wcag-audit-reporting.md` and `examples/skills/wcag-audit-reporting.md`

## Routing by Task Type

- **Reviewing a file for accessibility issues** → fixing-accessibility (primary) + wcag-audit-patterns + screen-reader-testing
- **Running a full WCAG audit** → wcag-audit-patterns (primary) + screen-reader-testing + fixing-accessibility + ui-visual-validator
- **Accessibility audit report** → wcag-audit-reporting (primary) + wcag-audit-patterns + screen-reader-testing + ui-visual-validator
- **Remediation backlog and retest** → wcag-audit-reporting (primary) + fixing-accessibility + screen-reader-testing
- **VPAT/ACR evidence support** → wcag-audit-reporting (primary) + wcag-audit-patterns + ui-visual-validator
- **Testing with screen readers** → screen-reader-testing (primary) + fixing-accessibility + wcag-audit-patterns
- **Assistive-tech edge-case investigation** → assistive-tech-edge-cases (primary) + screen-reader-testing + fixing-accessibility
- **High contrast / forced colors issue** → assistive-tech-edge-cases (primary) + ui-visual-validator + fixing-accessibility
- **Focus recovery after dynamic update** → assistive-tech-edge-cases (primary) + fixing-accessibility + screen-reader-testing
- **Speech or switch control issue** → assistive-tech-edge-cases (primary) + fixing-accessibility + ui-visual-validator
- **Verifying visual changes** → ui-visual-validator (primary) + fixing-accessibility + wcag-audit-patterns
- **Fixing animation jank** → fixing-motion-performance (primary) + fixing-accessibility + ui-visual-validator
- **Auditing page metadata/SEO** → fixing-metadata (primary) + ui-visual-validator
- **Building accessible components** → fixing-accessibility (primary) + wcag-audit-patterns + screen-reader-testing

## Shared Rules

- Read `../shared-rules/STYLE-GUARDRAILS.md` before delivering cross-mini-skill or package-level outputs.
- Read `../shared-rules/ANTI-PATTERNS.md` as final rejection checklist.

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
