# Skill Composition Protocol

## Package Structure

- `SKILL.md`
- `composition-protocol.md`
- `self-diagnostic-protocol.md`
- `resources/skill-catalog.md`
- `resources/routing-guide.md`
- `resources/asset-link-index.md`
- `resources/manifest.json`
- `references/skills/*.md`
- `examples/skills/*.md`

## Domain Coverage

This domain is not a single isolated task. Accessibility work is made of connected capabilities: auditing, remediation, assistive-technology testing, visual verification, motion safety, metadata correctness, and reporting.

Mini-skills are focused capabilities that route work to the right reference and example assets. `references/skills/*.md` provide operational methodology and constraints. `examples/skills/*.md` provide implementation and workflow patterns. Resource files provide routing, catalog, index, and machine-readable manifest support.

Do not treat mini-skills as isolated unless the task is truly narrow. Use this package as a routed domain system and compose mini-skills whenever the work has multiple moving parts.

## Universal Skill Composition Rule

For non-trivial tasks, compose mini-skills using this 5-step protocol:

1. Identify the single best primary mini-skill.
2. Identify at least two adjacent mini-skills.
3. Identify one validation mini-skill.
4. Open all selected files together before final answer when task has multiple moving parts.
5. Escalate if needed.

Minimum composition:
- 1 primary mini-skill
- 2 adjacent mini-skills
- 1 validation mini-skill

## Mini-Skill Selection Criteria

- **Relevance**: choose skills that directly match the user’s requested outcome.
- **Dependency**: include skills required to complete downstream steps safely.
- **Risk**: include skills that reduce legal, usability, and regression risk.
- **Validation**: include a skill that can independently verify claims with evidence.
- **Scale**: increase composition depth when scope spans multiple routes, components, or user flows.

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
