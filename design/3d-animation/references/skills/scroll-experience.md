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

### Production Failure Modes
- Scroll pinning shifts layout and causes cumulative layout shift spikes.
- Mobile viewport resize (URL bar collapse/expand) breaks trigger offsets.
- Reduced-motion users still receive motion-driven pinned storytelling.
- Keyboard-only navigation cannot access pinned sections predictably.
- Unmounted views leak ScrollTrigger/Lenis/listener subscriptions.

### Diagnostics Workflow (Scroll Experience)
1. Instrument pinned sections with markers and verify stable start/end positions across breakpoints.
2. Record CLS during full narrative scroll and flag spikes over the agreed budget.
3. Validate keyboard-only progression through interactive sections with focus visibility intact.
4. Toggle reduced-motion preference and verify non-animated fallback sequencing.
5. Navigate away and back repeatedly to confirm listener and trigger cleanup on unmount.

### Release Evidence Format
- Section timing table (section id, trigger start, trigger end, observed duration).
- CLS notes with measured totals and offending section references.
- Cleanup checklist covering listeners, ScrollTrigger instances, Lenis instances, and observers.
- Reduced-motion fallback description for each pinned segment.

### Acceptance / Rejection Criteria
- **Accept** when pinning retains layout stability within CLS budget.
- **Reject** if viewport resize produces drifted trigger alignment on mobile browsers.
- **Reject** when cleanup checks show retained listeners/triggers after route change.
- **Accept** only when reduced-motion and keyboard pathways preserve equivalent narrative access.

### Adjacent Mini-Skills to Use for Validation
- `threejs-animation`
- `threejs-fundamentals`
- `threejs-interaction`
