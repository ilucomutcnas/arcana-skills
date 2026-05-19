# assistive-tech-edge-cases

## Purpose
Detect and remediate failures that appear only under assistive-technology combinations, alternate input modes, accessibility settings, or stress conditions beyond baseline screen reader checks.

## When to Use
Use when core regression checks pass but production telemetry, support reports, or user testing reveal inconsistent failures across devices or accessibility settings.

## Required Inputs
- Critical user journeys with task completion definitions.
- Device/browser/accessibility-setting matrix.
- Findings from `screen-reader-testing` and `fixing-accessibility`.
- Motion behavior notes from `fixing-motion-performance`.
- Visual evidence plan from `ui-visual-validator`.

## Edge-Case Categories
Evaluate at minimum: speech control command targeting, switch control navigation order, screen magnification pan/focus coupling, high contrast/forced-colors tokens, browser zoom and text spacing, virtual cursor traps, live region overload behavior, focus recovery after dynamic updates, mobile gesture conflicts, and cognitive/time-sensitive interaction pressure.

## Testing Matrix Design
Build matrix columns for flow, AT/input mode, browser/OS setting, expected behavior, observed behavior, impact severity, and reproducibility confidence. Prioritize combinations with highest user share and highest risk flows.

## Acceptable vs Blocking Failures
Blocking failures prevent task completion, hide critical state, or create irreversible confusion. Acceptable failures are cosmetic and fully recoverable without additional cognitive load.

## Remediation Patterns
- Add explicit accessible names for speech command targets.
- Repair sequential focus model for switch users.
- Restore visible focus and semantic headings at high zoom.
- Use forced-colors-safe border tokens and `forced-color-adjust` rules.
- Throttle or dedupe live region announcements.
- Restore focus targets after async updates and modal closures.

## Integration and Rejection Criteria
Integrate with `screen-reader-testing`, `fixing-accessibility`, `fixing-motion-performance`, and `ui-visual-validator`. Reject conclusions that lack matrix evidence, severity rationale, remediation owner, or retest checklist.
