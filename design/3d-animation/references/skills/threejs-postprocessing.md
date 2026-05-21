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

### Mini-Skill-Specific Failure Modes
- incorrect pass order, oversized render targets, uncontrolled DPR cost, missing mobile disable path.

### Diagnostics Workflow
1. Build a minimal reproducible case centered on `threejs-postprocessing` behavior.
2. Validate configuration and lifecycle boundaries specific to this mini-skill.
3. Capture quantitative evidence (timings, memory, visual diffs) before and after fixes.
4. Verify fallback path behavior under failure and reduced-capability conditions.
5. Record release decision with explicit pass/fail against acceptance gates.

### Measurable Release Evidence
- Provide at least one table of baseline vs optimized measurements relevant to `threejs-postprocessing`.
- Validate on Chrome + Safari + Firefox and one mobile browser/GPU tier.
- Attach reproducible parameters/state values so QA can replay the scenario.

### Acceptance / Rejection Criteria
- **Accept** when all blocking defects are resolved, metrics meet budget, and fallback paths are confirmed.
- **Reject** when defect reproduction remains, metrics regress beyond threshold, or lifecycle cleanup/fallback is missing.

### Adjacent Mini-Skills to Use for Validation
- Primary validation neighbors: `procedural-shader-debugging`, `threejs-fundamentals`, and package-adjacent skills tied to `threejs-postprocessing`.
