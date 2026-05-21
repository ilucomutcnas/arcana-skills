---
name: "threejs-animation"
title: "Three.js Animation"
description: "Use for implementing Three.js procedural and keyframe animation using Timer, AnimationClip, AnimationMixer, and AnimationAction."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-animation.md`
- Examples: `examples/skills/threejs-animation.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for scene setup and animation loop
- Adjacent: `references/skills/threejs-loaders.md` — for loading animated GLTF models
- Adjacent: `references/skills/threejs-interaction.md` — for animation triggered by user input
- Validation: `references/skills/threejs-materials.md` — for animated material properties

## Purpose

Implement animation in Three.js using both procedural techniques (Timer, requestAnimationFrame) and the keyframe animation system (AnimationClip, AnimationMixer, AnimationAction). Covers keyframe track types, playback control, blending, and performance optimization.

## When to Use

- When animating Three.js objects with procedural motion (rotation, oscillation, orbiting)
- When playing back keyframe animations from GLTF models
- When creating custom AnimationClip sequences
- When blending or crossfading between animation states

## Workflow

1. Choose between procedural animation (Timer-based) and keyframe animation (AnimationClip-based).
2. For procedural: use `THREE.Timer()` (recommended in r183+) with `getDelta()` and `getElapsed()`.
3. For keyframe: create keyframe tracks, build an AnimationClip, attach to an AnimationMixer, and control playback via AnimationAction.
4. Update the mixer in the animation loop with `mixer.update(delta)`.
5. Optimize: share clips across mixers, call `clip.optimize()`, disable off-screen mixers.

## Quality Standards

- Share AnimationClips across multiple mixers when the same animation applies to multiple objects.
- Call `clip.optimize()` to remove redundant keyframes.
- Disable mixer updates for objects not visible on screen.
- Use LOD for animated characters at distance.
- Limit the number of active mixers — each `mixer.update()` has a cost.

## Technical Rules

- `AnimationClip`: container for keyframe data with a name and duration.
- `AnimationMixer`: plays animations on a root object. One mixer per animated object.
- `AnimationAction`: controls playback of a clip (play, pause, stop, crossfade, weight, time scale).
- Keyframe track types: NumberKeyframeTrack, VectorKeyframeTrack, QuaternionKeyframeTrack, ColorKeyframeTrack, BooleanKeyframeTrack, StringKeyframeTrack.
- Property paths use dot notation: `.position[y]`, `.material.opacity`, `.quaternion`.

## Validation

- Verify animations play at correct speed and loop as expected.
- Check that keyframe interpolation produces smooth transitions.
- Confirm mixer updates happen every frame in the animation loop.
- Test animation blending weights and crossfade timing.

## Restrictions

- Do not forget to call `mixer.update(delta)` in the animation loop.
- Do not create a new mixer every frame — create once and reuse.
- Do not use `THREE.Clock` for new projects — use `THREE.Timer` (r183+).

## Output Requirements

- Complete animation setup code with mixer, clips, and actions.
- Animation loop integration with delta time.
- Clear comments explaining track types and property paths.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Animation Failure Modes
- Mixer instances persist after scene teardown, leaking memory.
- Uncapped delta produces animation jumps after tab throttling.
- Clip blend weights snap due to misordered crossfade calls.
- Hidden-tab pause/resume resumes with invalid elapsed time.
- Reduced-motion mode still plays non-essential idle loops.

### Diagnostics Workflow (Mixer + Actions)
1. Document mixer/action lifecycle from model load through disposal.
2. Apply delta cap and compare motion continuity before/after.
3. Exercise clip transitions repeatedly to detect blend pops.
4. Run hidden-tab test (background 30s, return) and inspect continuity.
5. Validate reduced-motion behavior and confirm `uncacheRoot` cleanup.

### Release Evidence
- Mixer/action lifecycle table including cleanup steps.
- Hidden-tab test result note with observed behavior.
- Reduced-motion behavior summary for each animation channel.

### Acceptance Gates
- No leaked actions/mixers after route transitions.
- Blend transitions remain smooth under repeated interaction.
- Hidden-tab resume avoids jump artifacts.

### Validation Neighbors
- `threejs-loaders` for clip source integrity from GLTF.
- `threejs-interaction` for event-driven animation triggers.
- `threejs-fundamentals` for render-loop timing correctness.

