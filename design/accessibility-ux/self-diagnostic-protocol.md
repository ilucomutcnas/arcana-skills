# Self-Diagnostic Protocol

## Required Checks
- Confirm primary, adjacent, and validation mini-skills are explicitly listed.
- Map each issue to WCAG criterion and conformance level.
- Provide keyboard reproduction path evidence for operability claims.
- Provide AT/browser matrix evidence for screen reader or AT findings.
- Provide visual evidence for focus, contrast, target size, zoom, and text spacing behavior.
- Include reduced-motion and dynamic-update risk analysis when motion or async UI is changed.
- For audit outputs, include severity, owner, due date, remediation state, evidence pack, retest gate, and stakeholder summary.
- Confirm resource and asset index preservation, including existing linked folders and playbooks.

## Rejection Criteria
Reject outputs containing:
- remediation guidance without WCAG mapping;
- accessibility claims without keyboard path evidence;
- screen reader or AT conclusions without AT/browser matrix evidence;
- visual accessibility claims without focus/contrast evidence;
- motion changes without reduced-motion path and regression checks;
- audit reports missing severity, owner, retest, or evidence pack;
- deletion of existing asset-link-index entries or required resource links.
