# Skill Catalog

## 1. fixing-accessibility
- Summary: Remediate component-level accessibility failures across dialogs, menus, forms, tabs, accordions, icon-only buttons, live regions, and focus recovery.
- Reference: `references/skills/fixing-accessibility.md`
- Examples: `examples/skills/fixing-accessibility.md`
- Use with: `ui-visual-validator`, `screen-reader-testing`, `wcag-audit-reporting`

## 2. fixing-metadata
- Summary: Improve metadata quality for accessible titles, route context, locale alternates, canonical correctness, social previews, and JSON-LD consistency.
- Reference: `references/skills/fixing-metadata.md`
- Examples: `examples/skills/fixing-metadata.md`
- Use with: `ui-visual-validator`, `wcag-audit-reporting`

## 3. fixing-motion-performance
- Summary: Resolve animation jank and vestibular risks using reduced-motion governance, safe animation properties, and focus/scroll stability checks.
- Reference: `references/skills/fixing-motion-performance.md`
- Examples: `examples/skills/fixing-motion-performance.md`
- Use with: `assistive-tech-edge-cases`, `fixing-accessibility`

## 4. screen-reader-testing
- Summary: Execute structured test scripts across VoiceOver/NVDA/JAWS/TalkBack for navigation, forms, dialogs, tabs, and dynamic announcements.
- Reference: `references/skills/screen-reader-testing.md`
- Examples: `examples/skills/screen-reader-testing.md`
- Related assets:
  - `screen-reader-testing__resources/implementation-playbook.md`
- Use with: `assistive-tech-edge-cases`, `fixing-accessibility`, `wcag-audit-patterns`

## 5. ui-visual-validator
- Summary: Verify visual accessibility outcomes including focus ring visibility, contrast, hit targets, layout stability, zoom behavior, and forced-colors rendering.
- Reference: `references/skills/ui-visual-validator.md`
- Examples: `examples/skills/ui-visual-validator.md`
- Use with: `fixing-accessibility`, `fixing-metadata`

## 6. wcag-audit-patterns
- Summary: Execute WCAG 2.2 audit methodology with scope sampling, criterion mapping, automated/manual balance, and remediation sequencing.
- Reference: `references/skills/wcag-audit-patterns.md`
- Examples: `examples/skills/wcag-audit-patterns.md`
- Related assets:
  - `wcag-audit-patterns__resources/implementation-playbook.md`
- Use with: `wcag-audit-reporting` for full compliance audit delivery

## 7. wcag-audit-reporting
- Summary: Convert findings into governance-ready audit outputs with severity taxonomy, evidence packs, owner assignment, remediation backlog, and retest gates.
- Reference: `references/skills/wcag-audit-reporting.md`
- Examples: `examples/skills/wcag-audit-reporting.md`
- Use with: `wcag-audit-patterns`, `screen-reader-testing`, `ui-visual-validator`

## 8. assistive-tech-edge-cases
- Summary: Triage issues that appear only with combined assistive technologies, alternate input modes, forced-colors/high-zoom states, and dynamic-update stress conditions.
- Reference: `references/skills/assistive-tech-edge-cases.md`
- Examples: `examples/skills/assistive-tech-edge-cases.md`
- Use with: `screen-reader-testing`, `fixing-motion-performance`, `ui-visual-validator`

## Additional Package Index
- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
