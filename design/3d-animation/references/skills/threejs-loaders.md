---
name: "threejs-loaders"
title: "Three.js Loaders"
description: "Use for loading external assets in Three.js using GLTFLoader, TextureLoader, LoadingManager, and model post-processing."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-loaders.md`
- Examples: `examples/skills/threejs-loaders.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for scene setup
- Adjacent: `references/skills/threejs-materials.md` — for material adjustment on loaded models
- Adjacent: `references/skills/threejs-animation.md` — for playing loaded animation clips
- Validation: `references/skills/threejs-textures.md` — for texture loading patterns

## Purpose

Load external 3D models, textures, and other assets into Three.js scenes. Covers GLTFLoader, TextureLoader, LoadingManager for progress tracking, model traversal and post-processing, centering, and scaling.

## When to Use

- When loading GLTF/GLB 3D models
- When loading textures, cube maps, or HDR environment maps
- When implementing loading progress bars
- When post-processing loaded models (shadows, materials, centering, scaling)

## Workflow

1. Create a LoadingManager with onStart, onLoad, onProgress, and onError callbacks.
2. Instantiate loaders with the manager: GLTFLoader, TextureLoader, etc.
3. Load assets and handle the loaded data in callbacks or promises.
4. Post-process models: enable shadows, adjust materials, center and scale.
5. Add processed models to the scene.

## Quality Standards

- Always use LoadingManager for multi-asset loading with progress tracking.
- Traverse loaded models to enable shadows and adjust materials.
- Center and scale models using bounding box calculations.
- Handle loading errors gracefully with user feedback.

## Technical Rules

- GLTFLoader: loads `.gltf` and `.glb` files. Returns `{ scene, animations, cameras, asset }`.
- TextureLoader: loads image textures. Supports callback and synchronous-style APIs.
- LoadingManager: coordinates multiple loaders, fires callbacks for start, progress, completion, and errors.
- Model post-processing: use `model.traverse()` to iterate meshes, enable `castShadow` and `receiveShadow`, adjust materials.
- Centering: compute bounding box with `new THREE.Box3().setFromObject(model)`, get center, subtract from position.
- Scaling: compute max dimension from bounding box size, use `model.scale.setScalar(1 / maxDim)`.

## Validation

- Verify all assets load without errors.
- Confirm loading progress displays correctly.
- Check that models appear at correct position and scale.
- Test animation playback on loaded models with clips.

## Restrictions

- Do not load assets without error handling.
- Do not skip model centering and scaling for imported models.
- Do not forget to dispose loaded resources when removing them.

## Output Requirements

- Complete loader setup with LoadingManager.
- Model post-processing code (shadows, materials, centering).
- Error handling for all loading operations.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Production Failure Modes
- LoadingManager states do not progress cleanly from pending to complete/error.
- Failed model fetch leaves empty viewport without poster/model fallback.
- Imported GLTF scale/origin/orientation is inconsistent across assets.
- DRACO/KTX2 decoder pathways are misconfigured (without bundled binaries here).
- Requests cannot be cancelled during route changes, causing ghost updates.
- Cache strategy causes stale assets or redundant downloads on slow networks.

### Diagnostics Workflow (Three.js Loaders)
1. Trace LoadingManager callbacks and verify deterministic UI states.
2. Simulate 404/timeout failures and confirm fallback poster or fallback model path.
3. Normalize GLTF transforms at load time and record canonical orientation/scale rules.
4. Validate DRACO/KTX2 configuration notes and runtime capability checks.
5. Test cancellation on navigation and ensure in-flight callbacks are ignored safely.
6. Run throttled/offline network scenarios to verify release readiness.

### Release Evidence Format
- Loading state table (`idle`, `loading`, `partial`, `ready`, `error`) with UI behavior.
- Fallback result note describing exact behavior under fetch failure.
- Asset transform checklist (units, pivot, up-axis, scale normalization).
- Network failure test note for slow 3G and offline simulation.

### Acceptance / Rejection Criteria
- **Accept** when loading states and fallback behavior are user-visible and reliable.
- **Reject** if transform normalization is inconsistent between imported assets.
- **Reject** when cancelled requests can still mutate disposed scenes.
- **Accept** only when slow/offline scenarios are explicitly validated.

### Adjacent Mini-Skills to Use for Validation
- `threejs-textures`
- `threejs-materials`
- `threejs-animation`
