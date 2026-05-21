---
name: "scroll-experience"
title: "Scroll Experience"
description: "Use for building scroll-driven web animations using GSAP ScrollTrigger, Framer Motion, Locomotive Scroll, Lenis, and CSS scroll-timeline."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/scroll-experience.md`
- Examples: `examples/skills/scroll-experience.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for 3D scroll-linked scenes
- Adjacent: `references/skills/threejs-animation.md` — for animation timing patterns
- Validation: `references/skills/glsl-shader-alchemist.md` — for scroll-driven shader effects

## Purpose

Architect scroll-driven experiences that treat scrolling as a narrative device, not just navigation. Create moments of delight as users scroll — from subtle parallax to cinematic full-page transitions. Balance performance with visual impact.

## When to Use

- When creating scroll-based animations or parallax effects
- When building cinematic scrolling experiences
- When implementing scroll-linked 3D or canvas animations
- When choosing between scroll animation libraries for a project

## Workflow

1. Review design requirements and target platform.
2. Choose the appropriate scroll animation library based on project needs.
3. Set up smooth scrolling if needed (Lenis or Locomotive Scroll).
4. Implement scroll-triggered animations using the chosen library.
5. Test across breakpoints and devices for performance.
6. Validate accessibility — ensure content is usable without animations.

## Quality Standards

- Maintain 60fps during scroll animations.
- Provide fallbacks for users with `prefers-reduced-motion` enabled.
- Test on mobile devices — touch scrolling has different characteristics.
- Ensure content remains accessible without JavaScript.
- Use `will-change` and `transform` for GPU-accelerated animations.

## Technical Rules

Library options and their strengths:

- GSAP ScrollTrigger: best for complex, timeline-based scroll animations. Medium learning curve.
- Framer Motion: best for React projects with scroll-linked motion values. Low learning curve.
- Locomotive Scroll: best for smooth scroll + parallax combinations. Medium learning curve.
- Lenis: best for smooth scroll only, lightweight. Low learning curve.
- CSS scroll-timeline: best for simple, native scroll animations (2024+). Low learning curve.

## Validation

- Verify smooth 60fps performance during scroll.
- Test on multiple devices and screen sizes.
- Confirm `prefers-reduced-motion` support.
- Check that scroll position-linked animations sync correctly.

## Restrictions

- Do not create scroll-jacking that traps the user.
- Do not skip performance testing on mobile.
- Do not rely solely on scroll animations for critical content delivery.

## Output Requirements

- Provide complete, working scroll animation code.
- Include library import statements and setup.
- Document any performance considerations.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Scroll Production Failure Modes
- Pin sections introduce cumulative layout shift during hydration.
- Mobile viewport height changes break scroll timing offsets.
- Reduced-motion path missing, causing inaccessible long scrub animations.
- Keyboard users cannot progress narrative due to scroll-only triggers.
- ScrollTrigger/Lenis listeners survive unmount and double-fire on route return.

### Diagnostics Workflow (Narrative + Stability)
1. Build section timing table with start/end markers and pin ownership.
2. Record CLS during initial load and route transitions.
3. Run reduced-motion and keyboard-only traversal as mandatory accessibility pass.
4. Test mobile browser chrome show/hide to inspect viewport resize drift.
5. Verify teardown: destroy trigger instances and remove listeners on unmount.

### Evidence Required for Release Review
- Section timing table with intended visual events.
- CLS notes including measurement method and max observed value.
- Cleanup checklist results for listeners/triggers.
- Reduced-motion fallback description with screenshots optional (not stored in repo).

### Acceptance Gates
- CLS remains within project budget across target devices.
- Scroll narrative remains usable via keyboard and reduced-motion mode.
- No retained listeners or duplicate triggers after route remount.

### Validation Neighbors
- `threejs-animation` for scrubbed animation timing correctness.
- `threejs-fundamentals` for resize and render-loop resilience.
- `threejs-interaction` for keyboard/pointer parity validation.

