---
name: "spline-3d-integration"
title: "Spline 3D Integration"
description: "Use for embedding interactive 3D scenes from Spline.design into web projects with vanilla JS, React, Next.js, and Vue integration."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/spline-3d-integration.md`
- Examples: `examples/skills/spline-3d-integration.md`
- Guides: `spline-3d-integration__guides/VANILLA_INTEGRATION.md`, `spline-3d-integration__guides/REACT_INTEGRATION.md`, `spline-3d-integration__guides/PERFORMANCE.md`, `spline-3d-integration__guides/COMMON_PROBLEMS.md`
- Code examples: `spline-3d-integration__examples/vanilla-embed.html`, `spline-3d-integration__examples/react-spline-wrapper.tsx`, `spline-3d-integration__examples/interactive-scene.tsx`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for general 3D web context
- Adjacent: `references/skills/threejs-interaction.md` — for event handling patterns
- Validation: `references/skills/threejs-loaders.md` — for asset loading patterns

## Purpose

Master guide for embedding interactive 3D scenes from Spline.design into web projects. Covers vanilla HTML/JS embeds, React/Next.js/Vue integration, performance optimization, mobile considerations, and common debugging patterns.

## When to Use

- When embedding Spline 3D scenes into websites
- When integrating Spline with React, Next.js, or Vue
- When handling Spline event listeners and interaction
- When optimizing Spline scene performance for mobile
- When debugging Spline loading or rendering issues

## Workflow

1. Choose the integration approach based on the project framework:
   - Vanilla HTML/JS: see `spline-3d-integration__guides/VANILLA_INTEGRATION.md`
   - React / Next.js / Vue: see `spline-3d-integration__guides/REACT_INTEGRATION.md`
2. Embed the Spline scene using the scene URL (format: `https://prod.spline.design/XXXXXXXXXXXXXXXX/scene.splinecode`).
3. Configure interaction events as needed.
4. Optimize for performance: see `spline-3d-integration__guides/PERFORMANCE.md`.
5. Debug issues: see `spline-3d-integration__guides/COMMON_PROBLEMS.md`.

## Quality Standards

- Test scene loading across browsers and devices.
- Implement loading states while the 3D scene initializes.
- Handle errors gracefully when scenes fail to load.
- Optimize for mobile performance.

## Technical Rules

- Use the official `@splinetool/runtime` or `@splinetool/react-spline` packages.
- Scene URLs follow the format `https://prod.spline.design/<ID>/scene.splinecode`.
- Provide fallback content for environments where WebGL is not available.
- Lazy load Spline scenes below the fold.

## Validation

- Confirm scene loads and renders correctly in target browsers.
- Test interaction events fire as expected.
- Verify mobile performance is acceptable.
- Check that fallback content displays when WebGL is unavailable.

## Restrictions

- Do not embed excessively large Spline scenes without performance testing.
- Do not skip mobile testing.
- Do not hardcode scene URLs without configuration support.

## Output Requirements

- Complete integration code for the target framework.
- Loading and error state handling.
- Performance configuration when applicable.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Mini-Skill-Specific Failure Modes
- hydration mismatch in SSR, missing fallback poster, leaked event listeners, mobile framerate collapse.

### Diagnostics Workflow
1. Build a minimal reproducible case centered on `spline-3d-integration` behavior.
2. Validate configuration and lifecycle boundaries specific to this mini-skill.
3. Capture quantitative evidence (timings, memory, visual diffs) before and after fixes.
4. Verify fallback path behavior under failure and reduced-capability conditions.
5. Record release decision with explicit pass/fail against acceptance gates.

### Measurable Release Evidence
- Provide at least one table of baseline vs optimized measurements relevant to `spline-3d-integration`.
- Validate on Chrome + Safari + Firefox and one mobile browser/GPU tier.
- Attach reproducible parameters/state values so QA can replay the scenario.

### Acceptance / Rejection Criteria
- **Accept** when all blocking defects are resolved, metrics meet budget, and fallback paths are confirmed.
- **Reject** when defect reproduction remains, metrics regress beyond threshold, or lifecycle cleanup/fallback is missing.

### Adjacent Mini-Skills to Use for Validation
- Primary validation neighbors: `procedural-shader-debugging`, `threejs-fundamentals`, and package-adjacent skills tied to `spline-3d-integration`.
