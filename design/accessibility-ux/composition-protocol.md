# Composition Protocol

## Universal Composition Rule

For any non-trivial task, activate: (1) one primary execution skill, (2) one adjacent coverage skill, and (3) one validation/reporting skill.

## Workflow Recipes

1. **Full WCAG audit and report**
   - Primary: `wcag-audit-patterns`
   - Adjacent: `screen-reader-testing`
   - Validation/Output: `wcag-audit-reporting` + `ui-visual-validator`

2. **Component remediation and retest**
   - Primary: `fixing-accessibility`
   - Adjacent: `wcag-audit-patterns`
   - Validation/Output: `screen-reader-testing` + `wcag-audit-reporting`

3. **Screen reader compatibility investigation**
   - Primary: `screen-reader-testing`
   - Adjacent: `fixing-accessibility`
   - Validation/Output: `ui-visual-validator` + `wcag-audit-reporting`

4. **Assistive-tech edge-case triage**
   - Primary: `assistive-tech-edge-cases`
   - Adjacent: `screen-reader-testing` + `fixing-motion-performance`
   - Validation/Output: `ui-visual-validator`

5. **Motion accessibility remediation**
   - Primary: `fixing-motion-performance`
   - Adjacent: `assistive-tech-edge-cases` + `fixing-accessibility`
   - Validation/Output: `ui-visual-validator`

6. **Metadata and route UX validation**
   - Primary: `fixing-metadata`
   - Adjacent: `fixing-accessibility`
   - Validation/Output: `ui-visual-validator` + `wcag-audit-reporting`
