# Routing Guide

Use this guide to decide which extracted file to open.

## Rules

- Keep the main `SKILL.md` lightweight and navigational.
- Open `resources/skill-catalog.md` for the full index.
- Open `references/skills/<slug>.md` for the full methodology, guardrails, and validation rules.
- Open `examples/skills/<slug>.md` for sample commands, code, and usage patterns.
- If a task spans multiple domains, combine the relevant reference files instead of expanding the main `SKILL.md`.

## Quick Navigation

### Generative and Procedural Art
- **algorithmic-art** → `references/skills/algorithmic-art.md` and `examples/skills/algorithmic-art.md`

### Makepad Framework
- **makepad-animator** → `references/skills/makepad-animator.md` and `examples/skills/makepad-animator.md`
- **makepad-shader-lab** → `references/skills/makepad-shader-lab.md` and `examples/skills/makepad-shader-lab.md`

### Web Animation
- **scroll-experience** → `references/skills/scroll-experience.md` and `examples/skills/scroll-experience.md`

### Shader Programming
- **glsl-shader-alchemist** → `references/skills/glsl-shader-alchemist.md` and `examples/skills/glsl-shader-alchemist.md`
- **procedural-shader-debugging** → `references/skills/procedural-shader-debugging.md` and `examples/skills/procedural-shader-debugging.md`

### Third-Party 3D Tools
- **spline-3d-integration** → `references/skills/spline-3d-integration.md` and `examples/skills/spline-3d-integration.md`

### Three.js Core
- **threejs-fundamentals** → `references/skills/threejs-fundamentals.md` and `examples/skills/threejs-fundamentals.md`
- **threejs-geometry** → `references/skills/threejs-geometry.md` and `examples/skills/threejs-geometry.md`
- **threejs-materials** → `references/skills/threejs-materials.md` and `examples/skills/threejs-materials.md`
- **threejs-lighting** → `references/skills/threejs-lighting.md` and `examples/skills/threejs-lighting.md`
- **threejs-textures** → `references/skills/threejs-textures.md` and `examples/skills/threejs-textures.md`
- **threejs-loaders** → `references/skills/threejs-loaders.md` and `examples/skills/threejs-loaders.md`

### Three.js Advanced
- **threejs-animation** → `references/skills/threejs-animation.md` and `examples/skills/threejs-animation.md`
- **threejs-interaction** → `references/skills/threejs-interaction.md` and `examples/skills/threejs-interaction.md`
- **threejs-postprocessing** → `references/skills/threejs-postprocessing.md` and `examples/skills/threejs-postprocessing.md`
- **threejs-shader-forge** → `references/skills/threejs-shader-forge.md` and `examples/skills/threejs-shader-forge.md`

## Routing by Task Type

- **Starting a new 3D project** → threejs-fundamentals + threejs-geometry + threejs-materials + threejs-lighting
- **Adding user interaction** → threejs-interaction + threejs-fundamentals
- **Loading 3D models** → threejs-loaders + threejs-materials + threejs-animation
- **Custom visual effects** → threejs-shader-forge + glsl-shader-alchemist + threejs-postprocessing
- **Generative art** → algorithmic-art
- **Scroll animations** → scroll-experience
- **Embedding Spline scenes** → spline-3d-integration
- **Makepad UI work** → makepad-animator + makepad-shader-lab
- **Texture workflow** → threejs-textures + threejs-materials + threejs-loaders
- **Procedural shader bug** → procedural-shader-debugging + glsl-shader-alchemist + threejs-shader-forge
- **Mobile GPU shader artifact** → procedural-shader-debugging + glsl-shader-alchemist + threejs-materials + threejs-textures
- **Postprocessing pass-order issue** → procedural-shader-debugging + threejs-postprocessing + threejs-shader-forge
- **Color-space/tone-mapping mismatch** → procedural-shader-debugging + threejs-materials + threejs-postprocessing
- **Texture/material visual bug** → threejs-textures + threejs-materials + procedural-shader-debugging
- **Production 3D release review** → threejs-fundamentals + threejs-loaders + threejs-materials + threejs-textures + threejs-interaction + procedural-shader-debugging
- **Spline hero performance review** → spline-3d-integration + scroll-experience + threejs-fundamentals
- **Scroll scene performance/a11y review** → scroll-experience + threejs-animation + threejs-fundamentals

## Shared Rules

- Read `../shared-rules/STYLE-GUARDRAILS.md` before delivering cross-mini-skill work or package-level outputs.
- Read `../shared-rules/ANTI-PATTERNS.md` as a rejection checklist before final delivery.

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md) — complete link map for auxiliary folders and files.
- [`manifest.json`](manifest.json) — machine-readable package manifest.
