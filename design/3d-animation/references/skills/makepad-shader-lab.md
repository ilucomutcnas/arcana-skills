---
name: "makepad-shader-lab"
title: "Makepad Shader Lab"
description: "Use for writing Makepad custom pixel shaders using Sdf2d, uniforms, gradients, and rounded-box rendering."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/makepad-shader-lab.md`
- Examples: `examples/skills/makepad-shader-lab.md`

## Linked Package Files

- Adjacent: `references/skills/makepad-animator.md` — for animating shader uniforms
- Adjacent: `references/skills/glsl-shader-alchemist.md` — for general shader programming concepts
- Validation: `references/skills/threejs-fundamentals.md` — for rendering pipeline understanding

## Purpose

Provide expert guidance on Makepad shader authoring. Covers pixel shader functions, SDF-based shape rendering, uniform declarations, gradient mixing, and custom visual effects within the Makepad framework.

Version: makepad-widgets (dev branch). Last updated: 2026-01-19. Check for updates at https://crates.io/crates/makepad-widgets.

## When to Use

- When creating custom visual effects in Makepad using shader code
- When rendering SDF shapes such as rounded rectangles, circles, or custom geometry
- When implementing gradient fills, border effects, or procedural patterns
- When writing `fn pixel(self) -> vec4` functions in Makepad draw components

## Workflow

1. Enable the background shader with `show_bg: true` on the view.
2. Declare uniforms (colors, sizes, radii) before the shader function.
3. Create an SDF context using `Sdf2d::viewport(self.pos * self.rect_size)`.
4. Define shapes using SDF operations (box, circle, etc.).
5. Apply fills and strokes using `sdf.fill_keep()` and `sdf.stroke()`.
6. Return `sdf.result` or a custom `vec4` from the pixel function.

## Quality Standards

- Always use `show_bg: true` to enable background shader rendering.
- Use `Sdf2d::viewport()` to create the SDF context.
- Return `vec4` (RGBA) from `fn pixel()`.
- Declare uniforms before shader functions.
- Use `self.` prefix to access uniforms and built-in variables.

## Technical Rules

- Use Makepad and the official shader language.
- Uniforms are declared as properties in the draw component (e.g., `color: #FF0000`).
- Access built-in geometry via `self.pos`, `self.rect_size`.
- SDF operations: `sdf.box()`, `sdf.circle()`, `sdf.fill_keep()`, `sdf.stroke()`.
- Use `mix()` for color interpolation and gradients.

## Validation

- Confirm `show_bg: true` is set on all views using custom shaders.
- Verify all uniforms are declared and accessible via `self.` prefix.
- Check that `fn pixel()` returns a valid `vec4`.
- Test visual output across different widget sizes.

## Restrictions

- Do not skip visual inspection of shader output.
- Do not use undeclared uniforms inside shader functions.
- Do not omit `show_bg: true` — shaders will not render without it.

## Output Requirements

- Complete draw component blocks with shader code.
- All uniforms explicitly declared.
- Clear comments explaining SDF operations and visual intent.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Makepad Shader Failure Modes
- Sdf2d edges shimmer due to insufficient anti-alias window.
- Gradient banding in low-luminance themes.
- Rounded-box corners collapse when radius uniform overshoots control bounds.
- Uniform update cadence mismatched with animator state updates.
- Compile failure path leaves component blank instead of using visual fallback.

### Diagnostics Workflow (Sdf2d + Uniforms)
1. Visualize SDF distance field and edge threshold values while animating radius.
2. Run dark-theme gradient sweep and detect visible banding thresholds.
3. Log uniform writes per frame; verify ordering relative to animation state changes.
4. Force shader compile failure (invalid token test) to verify fallback paint path.
5. Compare before/after shader revisions with same interaction script.

### Required Release Evidence
- Before/after shader snippet showing artifact remediation.
- Artifact table (symptom, trigger, fix, residual risk).
- Uniform update checklist signed off for hover/focus/press transitions.

### Acceptance Gates
- No visible corner jitter in repeated hover loop.
- Gradient quality acceptable on at least one OLED mobile device class.
- Compile failure reliably switches to approved fallback style.

### Validation Neighbors
- `makepad-animator` for state transition timing alignment.
- `procedural-shader-debugging` for NaN/precision instrumentation patterns.
- `glsl-shader-alchemist` for shader math and anti-alias techniques.

