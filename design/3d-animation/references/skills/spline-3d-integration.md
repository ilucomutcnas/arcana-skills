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

### Production Failure Modes
- Spline payload blocks initial render because lazy loading gates are missing.
- Poster fallback does not render when WebGL init fails or bandwidth is constrained.
- Embedded scene listeners persist after component teardown.
- SSR/Next.js hydration mismatches occur from client-only Spline calls on server paths.
- Scene complexity exceeds mobile tier limits and causes thermal throttling.
- Accessibility alternative content is absent when 3D scene is unavailable.

### Diagnostics Workflow (Spline 3D Integration)
1. Verify lazy import boundaries so initial shell renders without scene payload.
2. Force offline/timeout conditions and confirm poster fallback plus actionable recovery messaging.
3. Audit event listener registration and disposal during mount/unmount cycles.
4. Test Next.js SSR routes to ensure Spline references are client-gated.
5. Benchmark scene tiers (low/medium/high complexity) on representative mobile hardware.
6. Validate accessible textual alternative and interactive controls parity.

### Release Evidence Format
- Lifecycle checklist for mount, ready, interaction, suspend, unmount, and disposal events.
- Mobile performance table (device tier, scene tier, FPS band, memory note).
- Fallback behavior notes covering offline, WebGL-fail, and reduced-capability scenarios.

### Acceptance / Rejection Criteria
- **Accept** when lazy loading preserves fast shell render and scene hydration is stable.
- **Reject** if listener cleanup is incomplete after route transitions.
- **Reject** if mobile low-tier profile cannot sustain declared performance target without fallback.
- **Accept** only when accessibility alternative content is present and meaningful.

### Adjacent Mini-Skills to Use for Validation
- `scroll-experience`
- `threejs-fundamentals`
- `threejs-loaders`
