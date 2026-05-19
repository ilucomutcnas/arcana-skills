# Skill Catalog

- `fixing-accessibility`: Component-level remediation for dialogs, menus, forms, tabs, accordions, icon-only controls, live regions, and focus recovery.
  - Use with: `ui-visual-validator`, `screen-reader-testing`, `wcag-audit-reporting`.
- `fixing-metadata`: Metadata governance for title quality, route announcements, canonical integrity, social previews, locale alternates, and structured data.
  - Use with: `ui-visual-validator`, `wcag-audit-reporting`.
- `fixing-motion-performance`: Motion safety and performance remediation with reduced-motion guarantees and dynamic update safeguards.
  - Use with: `assistive-tech-edge-cases`, `fixing-accessibility`.
- `screen-reader-testing`: Scripted screen reader verification across VoiceOver/NVDA/JAWS/TalkBack and virtual cursor vs focus mode.
  - Use with: `assistive-tech-edge-cases`, `fixing-accessibility`.
- `assistive-tech-edge-cases`: Cross-AT and alternate-input investigations for speech, switch, magnification, forced-colors, zoom, and gesture conflicts.
  - Use with: `screen-reader-testing`, `fixing-motion-performance`, `ui-visual-validator`.
- `ui-visual-validator`: Visual evidence checks for focus ring visibility, contrast, target size, layout shift, zoom/text-spacing resilience, and high-contrast rendering.
  - Use with: `fixing-accessibility`, `fixing-metadata`.
- `wcag-audit-patterns`: WCAG 2.2 audit methodology and criterion-level issue discovery.
  - Use with: `wcag-audit-reporting` for full compliance audit delivery.
- `wcag-audit-reporting`: Audit output governance, severity modeling, evidence packaging, remediation backlog ownership, and retest tracking.
  - Use with: `wcag-audit-patterns`, `screen-reader-testing`, `ui-visual-validator`.
