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

### Failure Modes for Makepad Animator State Systems
- Stuck state after rapid hover/press transitions.
- Disabled component still running hover pulse.
- Focus-ring transition conflicting with pressed transition keyframes.
- Hover/pressed race causing one-frame flicker or double transition.

### Diagnostics Workflow (State + Motion Tokens)
1. Build a transition matrix for `default`, `hover`, `pressed`, `focus`, `disabled`.
2. Mark each transition as `Snap` or `Forward` with rationale (latency-critical vs decorative).
3. Execute keyboard-only navigation to validate focus and reduced-motion behavior.
4. Stress-test pointer events (fast in/out + press spam) for race-condition artifacts.
5. Confirm disabled state suppresses animator channels except accessibility-indicator changes.

### Release Evidence Format
- State transition table with entry/exit triggers.
- Timing-token table (token name, ms, easing, Snap/Forward choice).
- Reduced-motion mapping note (what is removed, what remains semantic).

### Acceptance / Rejection Criteria
- Accept only if every state pair resolves deterministically without stuck values.
- Reject if disabled state animates, focus ring disappears, or transition races remain reproducible.
- Reject if reduced-motion mode still uses large-scale motion transforms.

### Validation Neighbors
- `makepad-shader-lab` for shader-uniform synchronization with animator state.
- `procedural-shader-debugging` when animated visual artifacts need instrumentation.

