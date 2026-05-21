---
name: "glsl-shader-alchemist"
title: "GLSL Shader Alchemist"
description: "Use for writing GPU shaders using GLSL for WebGL, Three.js, or game engines, covering vertex and fragment shaders, uniforms, and vector math."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/glsl-shader-alchemist.md`
- Examples: `examples/skills/glsl-shader-alchemist.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-shader-forge.md` — for Three.js-specific ShaderMaterial
- Adjacent: `references/skills/threejs-postprocessing.md` — for post-processing shader passes
- Adjacent: `references/skills/makepad-shader-lab.md` — for Makepad shader programming
- Validation: `references/skills/threejs-fundamentals.md` — for rendering pipeline context

## Purpose

Comprehensive guide to writing GPU shaders using GLSL (OpenGL Shading Language). Covers syntax, uniforms, varying variables, key mathematical concepts like swizzling and vector operations, and performance optimization for visual effects.

## When to Use

- When creating custom visual effects in WebGL, Three.js, or game engines
- When optimizing graphics rendering performance on the GPU
- When implementing post-processing effects (blur, bloom, color correction)
- When procedurally generating textures or geometry on the GPU

## Workflow

1. Identify whether a vertex shader, fragment shader, or both are needed.
2. Define uniforms for CPU-to-GPU data (time, resolution, colors).
3. Define varying variables for vertex-to-fragment data (UVs, normals).
4. Write the vertex shader to transform positions and pass data.
5. Write the fragment shader to compute final pixel colors.
6. Test visual output and iterate on parameters.

## Quality Standards

- Use `mix()` for linear interpolation instead of manual math.
- Use `step()` and `smoothstep()` for thresholding and soft edges — avoid `if` branches.
- Pack data into vectors (`vec4`) to minimize memory access.
- Do not use heavy branching (`if-else`) inside loops — it hurts GPU parallelism.
- Do not calculate constant values inside the shader — pre-calculate on the CPU using uniforms.

## Technical Rules

- GLSL data types: `float`, `vec2`, `vec3`, `vec4`, `mat2`, `mat3`, `mat4`, `sampler2D`.
- Swizzling: `vec.xy`, `vec.rgb`, `vec.xyzw` — reorder and extract components freely.
- Built-in functions: `mix()`, `step()`, `smoothstep()`, `clamp()`, `fract()`, `mod()`, `abs()`, `length()`, `normalize()`, `dot()`, `cross()`, `reflect()`.
- Vertex shader must set `gl_Position`.
- Fragment shader must set `gl_FragColor` (WebGL 1) or output variable (WebGL 2).
- Uniforms are read-only in shaders — set from JavaScript.
- Varyings interpolate between vertices automatically.

## Validation

- Verify visual output matches design intent.
- Check for shader compilation errors in the browser console.
- Profile GPU performance — avoid excessive texture lookups and branching.
- Test on multiple GPUs for compatibility.

## Restrictions

- Do not use heavy branching inside fragment shaders.
- Do not perform constant calculations inside shaders that could be pre-computed.
- Do not skip testing on lower-end GPUs.

## Output Requirements

- Provide complete vertex and fragment shader code.
- Include all uniform declarations with types and descriptions.
- Document any varying variables passed between stages.
- Include JavaScript setup code for uniform binding when relevant.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Production Failure Modes
- Precision qualifiers (`mediump`/`highp`) are inconsistent and create mobile artifacts.
- Derivative-based anti-aliasing (`fwidth`) is absent, causing shimmering edges.
- Dynamic branches inflate fragment cost on low-tier GPUs.
- Uniform contracts allow invalid ranges or missing defaults.
- Color-space assumptions conflict with tone-mapped output.
- Mobile GPUs fail compile/link due to unsupported instruction patterns.

### Diagnostics Workflow (GLSL Shader Alchemist)
1. Audit precision declarations per stage and verify mobile-safe fallback precision.
2. Run aliasing checks with and without derivative smoothing on thin features.
3. Profile branch-heavy paths and replace runtime branches with math/defines where needed.
4. Validate uniform schema (type, range, default, update cadence) against runtime inputs.
5. Compare linear vs sRGB output under active tone mapping across target browsers/GPUs.
6. Execute compile tests on at least one Adreno and one Apple GPU target class.

### Release Evidence Format
- Uniform validation table with name, type, legal range, default, and owner.
- Before/after shader snippet highlighting precision/AA/branch optimizations.
- Browser/GPU matrix documenting compile success and visual parity.
- Compile-time log excerpt or frame-cost delta note tied to the optimization.

### Acceptance / Rejection Criteria
- **Accept** only when shader compiles cleanly on documented desktop and mobile GPU matrix.
- **Reject** if uniform misuse can produce NaN output or clipped color without guardrails.
- **Reject** when branch-heavy code exceeds agreed frame-cost budget.
- **Accept** when color-space and tone-mapping behavior match art-direction references.

### Adjacent Mini-Skills to Use for Validation
- `procedural-shader-debugging`
- `threejs-shader-forge`
- `threejs-postprocessing`
