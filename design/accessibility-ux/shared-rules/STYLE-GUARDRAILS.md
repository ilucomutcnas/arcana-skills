# Accessibility UX Style Guardrails

These guardrails define shared output standards for all mini-skills in `design/accessibility-ux`. The aim is practical, testable accessibility guidance that improves user outcomes across interfaces and flows.

## 1) Use WCAG-aware language, not checklist theater
- Reference relevant WCAG success criteria when guidance depends on them.
- Describe conformance implications as practical impact, not as abstract labels alone.
- Avoid “AAA by default” framing unless explicitly required by project constraints.
- Keep wording actionable for designers, developers, QA, and content teams.

## 2) Center user impact in every recommendation
- Pair each issue with affected users (keyboard-only, low-vision, screen-reader users, motion-sensitive users, cognitive load concerns).
- Explain the task-level consequence (can’t submit form, loses context, misses status message).
- Prioritize blockers before comfort improvements.
- Include severity language tied to task completion and error risk.

## 3) Treat keyboard and screen-reader paths as first-class
- Specify tab order expectations for interactive regions.
- Require visible focus indicators with persistent contrast against nearby backgrounds.
- Define expected screen-reader announcements for labels, errors, and dynamic updates.
- Ensure escape, close, and return-focus behavior is described for dialogs/overlays.

## 4) Respect reduced-motion needs
- Include reduced-motion alternatives for non-essential animation.
- Distinguish decorative motion from task-critical feedback.
- Avoid direction that assumes motion improves clarity for all users.
- When motion is retained, constrain amplitude, duration, and frequency.

## 5) Maintain contrast and color discipline
- Do not rely on color as the only cue for state or meaning.
- Call for text/background contrast checks and non-text contrast checks where applicable.
- Require redundant cues: icon shape, text labels, position, or pattern.
- Flag low-contrast edge cases (disabled-looking active controls, stand-in-only labels).

## 6) Require semantic structure before ARIA augmentation
- Prefer native semantic elements for controls, headings, lists, tables, and form relationships.
- Use ARIA only when semantics cannot express required behavior.
- If ARIA is suggested, include expected role/name/state relationships to test.
- Avoid speculative claims like “screen-reader friendly” without validation steps.

## 7) Make recommendations testable
- Each fix should include a verification method:
  - keyboard-only flow test
  - screen-reader announcement check
  - contrast measurement
  - zoom/reflow test
  - reduced-motion preference test
- Keep pass criteria clear enough that QA can reproduce without interpretation.

## 8) Output format for cross-team execution
- Structure findings as: issue -> affected users -> recommended change -> verification.
- Separate immediate blockers from iterative enhancements.
- Keep guidance implementation-neutral when possible, but concrete enough to ship.

## Quick pre-delivery checklist
- [ ] WCAG-aware wording is specific and relevant.
- [ ] User impact is explicit for every issue.
- [ ] Keyboard and screen-reader behavior is defined.
- [ ] Reduced-motion handling is included where needed.
- [ ] Color is never the sole state indicator.
- [ ] Semantic structure is prioritized over ARIA patching.
- [ ] Every recommendation has a test method and pass criteria.
