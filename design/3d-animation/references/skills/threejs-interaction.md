---
name: "threejs-interaction"
title: "Three.js Interaction"
description: "Use for implementing Three.js user interaction with OrbitControls, raycasting, mouse picking, and click detection."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-interaction.md`
- Examples: `examples/skills/threejs-interaction.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for scene and camera setup
- Adjacent: `references/skills/threejs-animation.md` — for interaction-triggered animation
- Validation: `references/skills/threejs-geometry.md` — for collision meshes

## Purpose

Implement user interaction in Three.js scenes. Covers camera controls (OrbitControls), raycasting for object picking, mouse and touch event handling, drag interactions, and performance optimization for interactive scenes.

## When to Use

- When adding camera controls (orbit, pan, zoom) to a 3D scene
- When implementing click or hover detection on 3D objects
- When building drag-and-drop interactions in 3D space
- When handling mouse and touch events in Three.js

## Workflow

1. Set up OrbitControls for camera navigation.
2. Enable damping for smooth camera movement.
3. Create a Raycaster and mouse Vector2 for picking.
4. Normalize mouse coordinates to NDC (-1 to 1 range).
5. Cast rays from camera through mouse position.
6. Handle intersections for click, hover, or drag events.

## Quality Standards

- Throttle mousemove handlers to limit raycasts per frame.
- Use layers to filter raycast targets.
- Use simple invisible collision meshes for complex geometry.
- Disable controls when not needed.
- Batch interaction checks.

## Technical Rules

- `OrbitControls(camera, domElement)`: orbit, pan, zoom. Call `controls.update()` in the animation loop when damping is enabled.
- `Raycaster.setFromCamera(mouse, camera)`: cast ray from camera through mouse position.
- `Raycaster.intersectObjects(objects, recursive)`: returns sorted array of intersections.
- Intersection data: `distance`, `point` (world coords), `face`, `faceIndex`, `object`, `uv`, `normal`, `instanceId`.
- Mouse NDC conversion: `x = (clientX / width) * 2 - 1`, `y = -(clientY / height) * 2 + 1`.

## Validation

- Verify click detection works on all interactive objects.
- Test hover states highlight correctly.
- Confirm OrbitControls respond smoothly.
- Test on touch devices for mobile support.

## Restrictions

- Do not raycast every frame without throttling.
- Do not use complex geometry for raycasting — use simplified collision meshes.
- Do not forget to update controls in the animation loop when damping is on.

## Output Requirements

- Complete interaction setup with controls and raycasting.
- Mouse/touch event handlers with NDC conversion.
- Intersection handling with visual feedback.

## Production Constraints and Failure Modes

- Define measurable performance budgets (frame time, memory, draw calls, shader compile time) before implementation.
- Document browser/GPU matrix (Chrome, Safari, Firefox + at least one mobile device class) and known limitations.
- Add explicit fallback behavior (reduced motion, static poster, disabled heavy effect path) for low-end/mobile constraints.
- Capture failure modes in review notes: visual artifacts, precision drift, lifecycle leaks, disposal omissions, and asset loading errors.
- Require release evidence: before/after metrics, acceptance checklist, and rollback strategy.

## Diagnostics Checklist

1. Reproduce issue with minimal scene/component and deterministic inputs.
2. Isolate subsystem boundaries (geometry/material/shader/postprocessing/interaction/loader).
3. Instrument timing (`performance.now`, frame budget logging, renderer info counters).
4. Validate resize/dispose/context lifecycle and listener cleanup.
5. Verify color-space/tone mapping consistency and mobile-specific rendering behavior.
6. Record pass/fail evidence and ship only if all blocking defects are cleared.

