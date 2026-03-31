---
name: "threejs-shader-forge"
title: "Three.js Shader Forge"
description: "Use for creating custom Three.js ShaderMaterial and RawShaderMaterial with GLSL vertex and fragment shaders, uniforms, and TSL NodeMaterial."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-shader-forge.md`
- Examples: `examples/skills/threejs-shader-forge.md`

## Linked Package Files

- Adjacent: `references/skills/glsl-shader-alchemist.md` — for GLSL language fundamentals
- Adjacent: `references/skills/threejs-postprocessing.md` — for shader-based post-processing
- Adjacent: `references/skills/threejs-materials.md` — for built-in material alternatives
- Validation: `references/skills/threejs-fundamentals.md` — for rendering pipeline context

## Purpose

Create custom materials in Three.js using ShaderMaterial and RawShaderMaterial with GLSL vertex and fragment shaders. Also covers TSL (Three Shading Language) NodeMaterial for cross-renderer compatibility including WebGPU.

## When to Use

- When built-in materials cannot achieve the desired visual effect
- When writing custom vertex displacement or fragment coloring
- When porting existing GLSL shaders to Three.js
- When targeting WebGPU with TSL NodeMaterial
- When creating procedural textures or effects on the GPU

## Workflow

1. Choose between ShaderMaterial (includes Three.js built-in uniforms/attributes) and RawShaderMaterial (raw GLSL, declare everything).
2. Define uniforms object with types and initial values.
3. Write the vertex shader (set `gl_Position`).
4. Write the fragment shader (set `gl_FragColor`).
5. Update uniforms in the animation loop as needed.
6. For WebGPU support, consider TSL NodeMaterial instead.

## Quality Standards

- Minimize uniforms — group related values into vectors.
- Avoid conditionals in shaders — use `mix()` and `step()` instead.
- Pre-calculate values in JavaScript when possible.
- Use texture lookups for complex functions.
- Limit overdraw — avoid transparent shader materials when possible.

## Technical Rules

ShaderMaterial built-in uniforms (automatically available): modelMatrix, modelViewMatrix, projectionMatrix, viewMatrix, normalMatrix, cameraPosition.

ShaderMaterial built-in attributes (automatically available): position, normal, uv.

RawShaderMaterial: no built-in uniforms or attributes. Declare everything manually. Must include `precision` statement.

Choosing between approaches:
- GLSL ShaderMaterial: existing WebGL projects, maximum shader control, porting existing shaders.
- TSL NodeMaterial: new projects, WebGPU support needed, cross-renderer compatibility.

## Validation

- Check for shader compilation errors in the browser console.
- Verify uniform values update correctly at runtime.
- Test visual output matches design intent.
- Profile GPU performance for complex shaders.

## Restrictions

- Do not forget to update uniforms in the animation loop when they change.
- Do not use RawShaderMaterial without declaring all required uniforms and attributes.
- Do not skip precision statements in RawShaderMaterial.

## Output Requirements

- Complete ShaderMaterial or RawShaderMaterial setup.
- Vertex and fragment shader code.
- Uniform definitions and update logic.
- Comments explaining shader functionality.
