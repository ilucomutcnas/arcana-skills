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

### Interaction Failure Modes
- Raycasting every frame across all objects causes CPU spikes.
- Pointer normalization mismatch with canvas offsets yields inaccurate picks.
- Missing layer filtering allows non-interactive meshes to capture events.
- Touch flow diverges from pointer behavior.
- Keyboard alternative does not map to selected-object state.
- Event handlers accumulate across scene remounts.

### Diagnostics Workflow (Input Robustness)
1. Set raycast frequency budget and verify throttle/debounce behavior.
2. Validate pointer normalization using known screen-space test points.
3. Restrict raycast to interaction layers and verify exclusions.
4. Test pointer, touch, and keyboard parity for same target actions.
5. Audit listener attach/detach lifecycle during route transitions.

### Release Evidence Format
- Input-mode table (pointer/touch/keyboard behavior parity).
- Event lifecycle checklist (attach/remove points).
- Keyboard alternative validation notes for selection and focus announcement.

### Acceptance Gates
- Interaction latency remains within budget under expected object counts.
- Keyboard and touch users can complete core interactions.
- No stale listeners after unmount/remount cycles.

### Validation Neighbors
- `threejs-fundamentals` for resize/canvas coordinate consistency.
- `threejs-animation` for interaction-triggered motion behavior.
- `threejs-geometry` for accurate hit volumes and bounds.

