# assistive-tech-edge-cases
Use when baseline SR tests pass but production users fail under combined AT/input/settings.
Required inputs: critical flows, device/browser/AT matrix, recorded failure reports, WCAG map.
Edge-case categories: speech control, switch control, magnification, forced colors, zoom/text spacing, virtual cursor traps, live region overload, dynamic focus recovery, mobile gesture conflicts, cognitive/time-sensitive interactions.
Design matrix by flow x input mode x setting. Blocking failures are task-preventing or misleading outcomes; acceptable failures are cosmetic with preserved task completion.
Integrate with `screen-reader-testing`, `fixing-accessibility`, `fixing-motion-performance`, `ui-visual-validator`.
Reject if no matrix evidence, no remediation owner, or no retest checklist.
