# Skill Composition Protocol

## Package Structure
This package is a router over extracted mini-skills. `SKILL.md` stays lightweight; deep execution guidance lives in `references/skills/*.md` and `examples/skills/*.md`.

## Domain Coverage
Accessibility tasks span WCAG auditing, component remediation, metadata correctness, motion safety, screen reader validation, visual verification, audit reporting governance, and assistive-technology edge-case triage.

## Universal Skill Composition Rule
For any non-trivial task, compose mini-skills explicitly instead of using one in isolation.

### 1) Primary mini-skill selection
Select the mini-skill that best matches the primary deliverable:
- methodology/audit execution → `wcag-audit-patterns`
- remediation implementation → `fixing-accessibility`
- metadata correctness → `fixing-metadata`
- motion and vestibular safety → `fixing-motion-performance`
- SR workflow verification → `screen-reader-testing`
- visual evidence and regressions → `ui-visual-validator`
- report/governance output → `wcag-audit-reporting`
- combined AT/input/settings triage → `assistive-tech-edge-cases`

### 2) Adjacent mini-skill selection
Add at least one adjacent mini-skill that covers a likely failure surface not fully addressed by the primary skill.

### 3) Validation mini-skill selection
Add at least one validation/reporting mini-skill that produces independent acceptance evidence (`ui-visual-validator`, `screen-reader-testing`, or `wcag-audit-reporting`).

### 4) Escalation logic
Escalate composition when any of the following appear: dynamic UI updates, cross-browser inconsistencies, legal/compliance reporting requirements, conflicting AT results, or motion-related accessibility risks.

### 5) Minimum composition rule
Minimum acceptable composition for complex tasks: 1 primary + 1 adjacent + 1 validation mini-skill.

## Mini-Skill Selection Criteria
Use these criteria before finalizing composition:
- **Task objective:** audit, remediation, validation, or reporting.
- **Evidence requirement:** WCAG mapping, keyboard path, AT/browser matrix, visual/contrast evidence.
- **Risk profile:** blocking conversion flow, legal exposure, or broad component reuse.
- **Output audience:** engineering-only vs cross-functional stakeholder reporting.

## Accessibility Workflow Recipes
1. **Full WCAG audit and report**
   - Primary: `wcag-audit-patterns`
   - Adjacent: `screen-reader-testing`
   - Validation/Reporting: `ui-visual-validator` + `wcag-audit-reporting`
2. **Component remediation and retest**
   - Primary: `fixing-accessibility`
   - Adjacent: `wcag-audit-patterns`
   - Validation/Reporting: `screen-reader-testing` + `wcag-audit-reporting`
3. **Screen reader compatibility investigation**
   - Primary: `screen-reader-testing`
   - Adjacent: `fixing-accessibility`
   - Validation/Reporting: `ui-visual-validator` + `wcag-audit-reporting`
4. **Assistive-tech edge-case triage**
   - Primary: `assistive-tech-edge-cases`
   - Adjacent: `screen-reader-testing` + `fixing-motion-performance`
   - Validation/Reporting: `ui-visual-validator`
5. **Motion accessibility remediation**
   - Primary: `fixing-motion-performance`
   - Adjacent: `assistive-tech-edge-cases` + `fixing-accessibility`
   - Validation/Reporting: `ui-visual-validator`
6. **Metadata and route UX validation**
   - Primary: `fixing-metadata`
   - Adjacent: `fixing-accessibility`
   - Validation/Reporting: `ui-visual-validator` + `wcag-audit-reporting`
