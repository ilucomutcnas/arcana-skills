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

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Production Failure Modes
- Raycasts run every frame without throttling, causing CPU spikes.
- Pointer coordinates are mis-normalized under CSS scaling or DPR changes.
- Non-interactive objects are still included in raycast layers.
- Touch and keyboard alternatives are missing for pointer-only patterns.
- Event listeners persist after unmount.
- Focus state diverges from selected-object state.

### Diagnostics Workflow (Three.js Interaction)
1. Set raycast frequency budget per interaction type (hover, drag, click).
2. Validate pointer normalization math against resized canvas and DPR-capped renderer.
3. Enforce layer-based filtering so only intended objects participate in picking.
4. Verify parity across pointer, touch, and keyboard activation paths.
5. Audit event registration and cleanup on scene/controller lifecycle transitions.
6. Confirm focus and selection mappings remain synchronized for accessibility.

### Release Evidence Format
- Input-mode table listing supported actions for mouse, touch, keyboard, and assistive tech.
- Event lifecycle checklist covering add/remove points for all listeners.
- Keyboard alternative validation note with tested key bindings and focus outcomes.

### Acceptance / Rejection Criteria
- **Accept** when raycast workload stays inside budget under peak interaction.
- **Reject** if pointer normalization fails after resize or DPR changes.
- **Reject** when keyboard users cannot trigger primary interaction flows.
- **Accept** only when event cleanup prevents duplicate handlers after remount.

### Adjacent Mini-Skills to Use for Validation
- `threejs-fundamentals`
- `threejs-animation`
- `threejs-geometry`
