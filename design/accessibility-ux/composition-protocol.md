# Composition Protocol

## Universal Composition Rule
For non-trivial tasks, activate: (1) one primary execution mini-skill, (2) one adjacent coverage mini-skill, and (3) one validation/reporting mini-skill.

## Workflow Recipes
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
