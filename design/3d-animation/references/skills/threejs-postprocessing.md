---
name: "threejs-postprocessing"
title: "Three.js Post-Processing"
description: "Use for applying Three.js post-processing effects using EffectComposer, RenderPass, UnrealBloomPass, and custom shader passes."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-postprocessing.md`
- Examples: `examples/skills/threejs-postprocessing.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for renderer setup
- Adjacent: `references/skills/threejs-shader-forge.md` — for custom shader passes
- Adjacent: `references/skills/glsl-shader-alchemist.md` — for GLSL in custom passes
- Validation: `references/skills/threejs-materials.md` — for material interaction with effects

## Purpose

Apply post-processing effects to Three.js scenes using EffectComposer and render passes. Covers bloom, blur, color correction, FXAA, custom shader passes, and performance optimization.

## When to Use

- When adding bloom, glow, or halo effects
- When implementing color correction or grading
- When adding anti-aliasing as a post-processing step (FXAA)
- When creating custom full-screen shader effects
- When combining multiple effects in a render pipeline

## Workflow

1. Create an EffectComposer with the renderer.
2. Add RenderPass as the first pass (renders the scene).
3. Add effect passes (UnrealBloomPass, ShaderPass, etc.).
4. The last pass renders to screen by default.
5. In the animation loop, call `composer.render()` instead of `renderer.render()`.
6. Handle window resize: update both renderer and composer sizes.

## Quality Standards

- Limit the number of passes — each adds a full-screen render.
- Use lower resolution render targets for blur passes.
- Disable unused effects by toggling `pass.enabled`.
- Use FXAA over MSAA when possible — less expensive.
- Profile GPU usage with browser DevTools.

## Technical Rules

- EffectComposer replaces `renderer.render()` in the animation loop.
- RenderPass must be the first pass.
- UnrealBloomPass(resolution, strength, radius, threshold): glow effect.
- ShaderPass: apply custom shaders as full-screen effects.
- Handle resize by calling both `renderer.setSize()` and `composer.setSize()`.

## Validation

- Confirm effects render as expected visually.
- Verify performance stays at 60fps with all active passes.
- Test resize handling updates all render targets.
- Check that bloom threshold and strength produce the desired glow.

## Restrictions

- Do not forget to replace `renderer.render()` with `composer.render()`.
- Do not add passes without profiling their performance impact.
- Do not skip resize handling for the composer.

## Output Requirements

- Complete EffectComposer setup with RenderPass and effect passes.
- Animation loop using `composer.render()`.
- Resize handler for both renderer and composer.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Post Stack Failure Modes
- Incorrect pass ordering causes halo clipping or broken depth cues.
- Render targets sized above practical budget for device tier.
- DPR left uncapped while heavy bloom is active.
- Bloom threshold poorly tuned, crushing midtones.
- OutputPass/tone mapping mismatched with renderer color pipeline.
- Mobile path lacks post stack disable/degrade decision.

### Diagnostics Workflow (Composer Integrity)
1. Document pass order with dependencies (input/output expectations).
2. Measure per-pass GPU cost and total post-processing overhead.
3. Validate render-target sizing against DPR caps per tier.
4. Tune bloom threshold/intensity using reference shots.
5. Confirm OutputPass and tone mapping are applied once in final pipeline.
6. Test mobile disable path and fallback visual quality.

### Release Evidence
- Pass-order table with rationale.
- Render-target budget note (resolution + DPR policy).
- Mobile disable decision and trigger conditions.
- Before/after frame-cost note from profiler pass.

### Acceptance Gates
- Post stack cost stays within allocated frame budget.
- Color output remains consistent with non-post baseline intent.
- Mobile fallback maintains legibility without severe artifacting.

### Validation Neighbors
- `threejs-shader-forge` for custom pass shader correctness.
- `procedural-shader-debugging` for artifact isolation.
- `threejs-fundamentals` for renderer/tone-mapping consistency.

