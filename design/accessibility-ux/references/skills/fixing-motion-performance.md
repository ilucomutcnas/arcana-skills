---
name: "fixing-motion-performance"
title: "Fixing Motion Performance"
description: "Use for diagnosing and fixing animation performance issues including layout thrashing, composite layer promotion, FLIP patterns, scroll-linked motion, and reduced-motion preferences."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/fixing-motion-performance.md`
- Examples: `examples/skills/fixing-motion-performance.md`

## Linked Package Files

- Adjacent: `references/skills/fixing-accessibility.md` — for reduced-motion and accessibility concerns
- Adjacent: `references/skills/ui-visual-validator.md` — for verifying visual output of animations
- Validation: `references/skills/wcag-audit-patterns.md` — for WCAG 2.2.2 motion requirements

## Purpose

Fix animation performance issues in web UIs. Covers layout thrashing, composite layer promotion, the FLIP technique, scroll-linked animation, CSS vs JavaScript animation tradeoffs, and respecting prefers-reduced-motion.

## When to Use

- When adding or changing UI animations (CSS, WAAPI, Framer Motion, rAF, GSAP)
- When refactoring janky interactions or transitions
- When implementing scroll-linked motion or reveal-on-scroll
- When animating layout properties, filters, masks, gradients, or CSS variables
- When reviewing components that use will-change, transforms, or layout measurement

## Workflow

1. Review the file or component against motion performance rules.
2. For each violation found, quote the exact line or snippet.
3. Explain why it matters in one short sentence.
4. Provide a concrete code-level fix.
5. Do not migrate animation libraries unless explicitly requested — apply rules within the existing stack.

## Quality Standards

- Animate only composite properties (transform, opacity) whenever possible.
- Never animate layout properties (width, height, top, left, margin, padding) directly.
- Batch DOM reads before DOM writes to avoid layout thrashing.
- Use the FLIP technique for layout animations that cannot avoid geometry changes.
- Prefer CSS scroll-timeline over JavaScript scroll listeners.
- Respect prefers-reduced-motion: reduce for all non-essential animations.

## Technical Rules

- Composite-friendly properties: transform, opacity, filter (GPU-accelerated).
- Layout-triggering properties: width, height, top, left, margin, padding, border.
- Use will-change sparingly — apply only to elements about to animate, remove after.
- FLIP: First (measure), Last (apply final state), Invert (calculate delta), Play (animate).
- Use requestAnimationFrame for JS-driven animations, never setTimeout or setInterval.

## Validation

- Verify animations run at 60fps using browser DevTools performance panel.
- Confirm no layout thrashing occurs during animation.
- Test prefers-reduced-motion behavior.
- Check that will-change is not applied permanently to many elements.

## Restrictions

- Do not migrate animation libraries unless explicitly requested.
- Do not suppress prefers-reduced-motion preferences.
- Do not apply will-change permanently — it consumes GPU memory.

## Output Requirements

- List each performance violation with exact line or snippet.
- Provide a one-sentence impact explanation.
- Provide a concrete code-level fix.
