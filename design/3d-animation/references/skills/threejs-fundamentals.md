---
name: "threejs-fundamentals"
title: "Three.js Fundamentals"
description: "Use for setting up Three.js core infrastructure including scene, camera, renderer, fog, import maps, responsive resize, and animation loop."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-fundamentals.md`
- Examples: `examples/skills/threejs-fundamentals.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-geometry.md` — for creating 3D shapes
- Adjacent: `references/skills/threejs-materials.md` — for material configuration
- Adjacent: `references/skills/threejs-lighting.md` — for scene lighting
- Validation: `references/skills/threejs-interaction.md` — for camera controls and input

## Purpose

Systematically create high-quality 3D scenes and interactive experiences using Three.js best practices. Covers scene initialization, camera setup, renderer configuration, fog, background, responsive layout, and the animation loop.

## When to Use

- When starting a new Three.js project
- When setting up scene, camera, and renderer infrastructure
- When configuring responsive canvas layout with window resize handling
- When establishing the animation loop
- When creating 3D visualizations, interactive experiences, or WebGL applications

## Workflow

1. Set up import map or module imports for Three.js and addons.
2. Create the scene, camera (PerspectiveCamera or OrthographicCamera), and renderer.
3. Configure renderer settings: antialiasing, pixel ratio, size.
4. Add the renderer DOM element to the page.
5. Set scene background, environment map, and fog if needed.
6. Position the camera and optionally add OrbitControls.
7. Create the animation loop with `requestAnimationFrame` or `renderer.setAnimationLoop`.
8. Add window resize handler to update camera aspect ratio and renderer size.

## Quality Standards

- Limit draw calls: merge geometries, use instancing, atlas textures.
- Ensure bounding boxes are correct for frustum culling (enabled by default).
- Use `THREE.LOD` for distance-based mesh switching.
- Object pooling: reuse objects instead of creating and destroying.
- Avoid `getWorldPosition()` in loops — cache results.
- Set `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))` to cap resolution.

## Technical Rules

- Use import maps for browser-based projects: map `"three"` to CDN URL.
- Use `THREE.PerspectiveCamera(fov, aspect, near, far)` for most 3D scenes.
- Call `camera.updateProjectionMatrix()` after changing fov, aspect, near, or far.
- Scene properties: `scene.background` (Color, Texture, CubeTexture), `scene.environment` (env map for PBR), `scene.fog` (Fog or FogExp2).
- Version: Three.js r183+ recommended. Import from `https://cdn.jsdelivr.net/npm/three@0.183.0/`.

## Validation

- Confirm the scene renders at 60fps.
- Verify responsive resize works correctly.
- Check that the animation loop runs and updates are applied.
- Test on multiple browsers for WebGL compatibility.

## Restrictions

- Do not use deprecated `THREE.Geometry` — use `THREE.BufferGeometry`.
- Do not forget responsive resize handler.
- Do not set pixel ratio above 2 — diminishing returns with high GPU cost.
- Do not use `THREE.CapsuleGeometry` before r142.

## Output Requirements

- Complete scene setup with scene, camera, renderer, and animation loop.
- Responsive resize handler.
- Import statements or import map configuration.
- Clear comments explaining each setup step.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Mini-Skill-Specific Failure Modes
- resize drift, context-loss unrecovered, excessive DPR causing GPU overload, SSR/client boundary leaks.

### Diagnostics Workflow
1. Build a minimal reproducible case centered on `threejs-fundamentals` behavior.
2. Validate configuration and lifecycle boundaries specific to this mini-skill.
3. Capture quantitative evidence (timings, memory, visual diffs) before and after fixes.
4. Verify fallback path behavior under failure and reduced-capability conditions.
5. Record release decision with explicit pass/fail against acceptance gates.

### Measurable Release Evidence
- Provide at least one table of baseline vs optimized measurements relevant to `threejs-fundamentals`.
- Validate on Chrome + Safari + Firefox and one mobile browser/GPU tier.
- Attach reproducible parameters/state values so QA can replay the scenario.

### Acceptance / Rejection Criteria
- **Accept** when all blocking defects are resolved, metrics meet budget, and fallback paths are confirmed.
- **Reject** when defect reproduction remains, metrics regress beyond threshold, or lifecycle cleanup/fallback is missing.

### Adjacent Mini-Skills to Use for Validation
- Primary validation neighbors: `procedural-shader-debugging`, `threejs-fundamentals`, and package-adjacent skills tied to `threejs-fundamentals`.
