# Self-Diagnostic Protocol

## Required Checks

- Confirm primary, adjacent, and validation mini-skills are explicitly activated.
- Map each reported issue to WCAG criterion ID and level.
- Include keyboard reproduction path for every operability issue.
- Include screen reader / AT browser matrix evidence for AT claims.
- Include visual evidence for focus, contrast, hit target, zoom/text-spacing behavior.
- Include reduced-motion and dynamic-update risk assessment for motion or async UI changes.
- Confirm audit report completeness: severity, owner, due date, remediation status, retest gate, evidence pack.
- Confirm `resources/asset-link-index.md` and manifest links preserve existing entries.

## Rejection Criteria

Reject output if any apply:
- remediation guidance without WCAG mapping;
- accessibility claims without keyboard path evidence;
- screen reader conclusions without AT/browser matrix;
- visual accessibility fixes without focus/contrast evidence;
- motion changes without reduced-motion fallback path;
- audit report missing severity, owner, retest plan, or evidence pack;
- deletion of existing resource/index links or asset entries.
