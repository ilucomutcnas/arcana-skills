---
name: "makepad-animator"
title: "Makepad Animator"
description: "Use for implementing Makepad animation states and transitions with forward timing, snap changes, and shader uniform animation."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/makepad-animator.md`
- Examples: `examples/skills/makepad-animator.md`

## Linked Package Files

- Adjacent: `references/skills/makepad-shader-lab.md` — for shader-based visual effects in animated elements
- Validation: `references/skills/threejs-fundamentals.md` — for general animation timing concepts

## Purpose

Provide expert guidance on Makepad animation patterns. Covers writing animation code, explaining states and transitions, and implementing responsive UI animations using the Makepad framework.

Version: makepad-widgets (dev branch). Last updated: 2026-01-19. Check for updates at https://crates.io/crates/makepad-widgets.

## When to Use

- When building Makepad UI animations with hover, focus, pressed, or custom state transitions
- When implementing smooth forward transitions or instant snap state changes
- When animating shader uniforms in `draw_bg`, `draw_text`, or other draw components

## Workflow

1. Define the animator block inside the widget declaration.
2. Set the `default:` state for initial appearance.
3. Use `Forward` for smooth animated transitions with a specified duration.
4. Use `Snap` for instant state changes (such as disabled states).
5. Keep durations short (0.1–0.3s) for a responsive feel.
6. Animate shader uniforms in `draw_bg`, `draw_text`, and related draw components.

## Quality Standards

- Always set `default:` for initial state in every animator group.
- Use `Forward` for user-perceptible transitions.
- Use `Snap` for instantaneous state changes.
- Keep transition durations between 0.1s and 0.3s for responsive UI feel.
- Follow Makepad framework conventions and community standards.

## Technical Rules

- Use Makepad and the official makepad-widgets ecosystem.
- Avoid deprecated APIs or unmaintained libraries.
- Pin dependency versions for reproducible builds.
- Animator groups must always declare a `default` state.
- Apply transitions using `from: { all: Forward { duration: X } }` or `from: { all: Snap }`.

## Validation

- Verify all animator states have a `default` declared.
- Confirm all transitions use appropriate timing (Forward or Snap).
- Check that all animated properties map to valid shader uniforms.
- Test hover, focus, and pressed states for correct visual feedback.

## Restrictions

- Do not skip visual inspection of the final animation output.
- Do not mix incompatible design frameworks with Makepad.
- Do not hardcode values that should be configurable through uniforms.

## Output Requirements

- Provide complete animator blocks with all required states.
- Include clear comments explaining each state and transition.
- Use consistent formatting following Makepad DSL conventions.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Production Failure Modes
- Animator state machine remains latched after quick hover→pressed→disabled transitions.
- `Snap` is used where `Forward` is required, causing abrupt UI regressions.
- Disabled controls still animate hover/pressed tracks.
- Focus ring animation conflicts with pressed timeline and obscures accessibility state.
- Hover and pressed signals race, producing nondeterministic keyframe selection.

### Diagnostics Workflow (Makepad Animator)
1. Document each widget state node and allowed transitions (`idle`, `hover`, `focus`, `pressed`, `disabled`).
2. Audit per-transition timing mode and justify `Snap` vs `Forward` in a rule table.
3. Simulate rapid pointer/key navigation to surface hover/pressed race behavior.
4. Verify disabled-state precedence: once disabled, all non-essential animations must stop.
5. Execute reduced-motion pass and confirm every animated transition maps to compliant alternatives.

### Release Evidence Format
- State transition table covering source state, target state, guard condition, and transition mode.
- Timing-token table listing duration/ease tokens and where they are consumed.
- Reduced-motion mapping note describing per-state fallback behavior.

### Acceptance / Rejection Criteria
- **Accept** when every interaction path resolves to a valid terminal state without deadlocks.
- **Reject** if disabled components animate or process hover/pressed tracks.
- **Reject** if focus indicator timing can be visually masked by pressed transitions.
- **Accept** only when reduced-motion behavior preserves affordance clarity without motion-heavy sequences.

### Adjacent Mini-Skills to Use for Validation
- `makepad-shader-lab`
- `procedural-shader-debugging`
