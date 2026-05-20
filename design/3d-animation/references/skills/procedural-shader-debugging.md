---
name: "procedural-shader-debugging"
title: "Procedural Shader Debugging"
description: "Diagnose and remediate broken procedural visuals across GLSL, Three.js shader materials, Makepad shaders, and post-processing pipelines."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "20.05.2026"
---

## Purpose

Use this mini-skill when shader-driven visuals are incorrect, unstable, inconsistent across GPUs, or failing release gates.

## Required Inputs

- Minimal reproduction link or code snippet.
- Expected visual behavior and blocking symptoms.
- Runtime stack (Three.js/WebGL/WebGPU/Makepad/postprocessing passes).
- Browser and GPU matrix, including at least one mobile device class.

## Debugging Taxonomy

- Compile/link errors.
- Uniform/time drift and update-order mistakes.
- Coordinate-space mismatch (object/world/view/clip/UV).
- UV/normal/tangent mistakes.
- Precision issues (`mediump` vs `highp`) and mobile GPU differences.
- NaNs/infinities caused by invalid math (`normalize(0)`, divide by zero, invalid pow).
- Color-space and tone-mapping mismatch.
- Derivative/aliasing artifacts (`fwidth`, mip bias, temporal shimmer).
- Render target resolution mismatch / DPR mismatch.
- Depth/normal buffer mistakes.
- Post-processing pass-order errors.

## Diagnostic Workflow

1. Build a minimal repro with single mesh/material/pass and fixed uniforms.
2. Validate compile and link logs first.
3. Instrument shader outputs (channel packing, normal-as-color, UV heatmap, NaN sentinels).
4. Freeze time/uniform updates to detect drift or race conditions.
5. Validate spaces (UV, world, view) at each stage.
6. Compare with/without postprocessing and with forced DPR=1.
7. Check mobile precision path and texture format compatibility.
8. Produce release evidence (before/after, matrix, pass/fail gates).

## Instrumentation Techniques

- Replace final color with debug buffers (`vec3(uv,0)`, `normal*0.5+0.5`, depth ramps).
- Inject guard math: clamp denominators, epsilon thresholds, finite checks.
- Add per-pass toggles and pass-order switches.
- Use browser shader logs and renderer info without committing binary frame captures.

## Acceptance vs Blocking Defects

Acceptable: minor non-blocking noise below documented threshold and not visible in normal viewing distance.
Blocking: NaN flashing, severe banding, color-space mismatch, pass-order artifacts, mobile-only breakage, or unstable animation.

## Integration Boundaries

- Pair with `glsl-shader-alchemist` for shader authoring fixes.
- Pair with `threejs-shader-forge` for ShaderMaterial/RawShaderMaterial/TSL lifecycle.
- Pair with `makepad-shader-lab` for Makepad shader diagnostics.
- Pair with `threejs-postprocessing` for composer pass defects.
- Pair with `threejs-materials` and `threejs-textures` for material/texture mismatch root causes.

## Rejection Criteria

Reject output if it lacks minimal repro, before/after evidence, browser/GPU matrix, or explicit fallback/rollback path.
