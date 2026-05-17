# Accessibility UX Anti-Patterns

This anti-pattern list helps mini-skills in `design/accessibility-ux` avoid superficial or non-testable outputs. Use it as a rejection filter before delivering recommendations.

## 1) Treating accessibility as visual polish
**Pattern:** Accessibility guidance appears only in final visual cleanup notes.

**Why it fails:** Structural barriers remain in interaction logic, semantics, and error handling.

**Better approach:** Address accessibility during information architecture, interaction design, and component behavior decisions.

## 2) Relying only on color for meaning
**Pattern:** States are differentiated only by hue changes (success/error/active/disabled).

**Why it fails:** Many users cannot reliably detect these differences, especially in low contrast or color-vision variance.

**Better approach:** Add redundant cues (text, iconography, shape, position, or patterns) and verify contrast requirements.

## 3) Vague “make it accessible” directives
**Pattern:** Recommendations like “improve accessibility” or “ensure WCAG compliance” with no concrete action.

**Why it fails:** Teams cannot implement or validate broad instructions.

**Better approach:** Provide scoped, testable changes tied to a specific component, flow, or success criterion.

## 4) Untested ARIA confidence
**Pattern:** Declaring a pattern accessible because ARIA attributes were added.

**Why it fails:** Incorrect role/name/state mappings or focus handling can still break assistive technology behavior.

**Better approach:** Prefer semantic HTML first; when ARIA is needed, include explicit keyboard and announcement verification steps.

## 5) Ignoring keyboard interaction paths
**Pattern:** Solutions optimize pointer interactions but omit tab order, focus trap, and key commands.

**Why it fails:** Keyboard-only users face dead ends or context loss.

**Better approach:** Define complete keyboard flows including entry, navigation, activation, dismissal, and focus return.

## 6) Overusing motion as primary feedback
**Pattern:** Critical state changes depend on animations, parallax, or timed transitions.

**Why it fails:** Motion-sensitive users and reduced-motion contexts may miss or avoid essential information.

**Better approach:** Provide static equivalents and make state changes perceptible without animation.

## 7) Missing user impact framing
**Pattern:** Findings list technical defects without explaining who is blocked or confused.

**Why it fails:** Prioritization becomes arbitrary and remediation stalls.

**Better approach:** Link each issue to affected users and task consequences.

## 8) Recommendations without verification criteria
**Pattern:** “Fix labels” or “improve focus” with no expected outcome.

**Why it fails:** QA cannot confirm completion and regressions recur.

**Better approach:** Add measurable pass conditions for keyboard, screen-reader, contrast, zoom/reflow, and reduced-motion checks.

## Anti-pattern rejection checklist
- [ ] No accessibility guidance limited to visual polish.
- [ ] No color-only status communication.
- [ ] No vague accessibility mandates without concrete actions.
- [ ] No unverified ARIA assertions.
- [ ] No keyboard flow gaps.
- [ ] No motion-dependent critical feedback.
- [ ] No issue lacking explicit user impact.
- [ ] No recommendation missing test criteria.
