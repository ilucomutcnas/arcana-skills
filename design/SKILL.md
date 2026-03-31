---
name: "3d-animation"
title: "3D & Animation Studio"
description: "Use for 3D graphics, WebGL rendering, Three.js scenes, GLSL shaders, Makepad animations, Spline 3D embeds, scroll-driven animations, p5.js generative art, procedural animation, post-processing effects, and adjacent tasks involving interactive visual experiences on the web."
version: "1.0.0"
category: "Design"
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---
 
## Purpose
 
Provide structured guidance for creating 3D graphics, animations, shader programs, and interactive visual experiences on the web. This domain covers Three.js scene creation, GLSL and Makepad shader authoring, Spline 3D embedding, scroll-driven animations, and p5.js generative art.
 
## Domain Coverage
 
This package represents the 3D and animation domain for web development. It covers multiple interconnected capabilities: scene setup, geometry, materials, lighting, textures, loaders, interaction, animation, post-processing, shader programming, generative art, scroll effects, and third-party 3D tool integration.
 
Mini-skills are separated for routing and selective loading. Real tasks in this domain rarely depend on one skill alone — building a complete 3D experience typically requires combining scene setup with materials, lighting, interaction, and possibly post-processing or custom shaders.
 
## How to Use
 
1. Always begin with self-diagnostic. Start with a quick package integrity check, then validate only the activated working set. The self-diagnostic rules are defined in `self-diagnostic-protocol.md`.
2. Identify the primary mini-skill that best matches the task.
3. Check the Multi-Skill Activation Guide below to load adjacent mini-skills that commonly co-occur with the primary task.
4. Open the corresponding reference file under `references/skills/`.
5. Open the corresponding examples file under `examples/skills/` if concrete code is needed.
6. Use `resources/skill-catalog.md` for the full index.
7. Use `resources/routing-guide.md` when a task spans multiple mini-skills.
8. Use `resources/asset-link-index.md` to find every auxiliary folder and file.
 
## Multi-Skill Activation Guide
 
Do not treat mini-skills as isolated when the task spans multiple concerns. For all non-trivial tasks, apply the universal composition rule in `composition-protocol.md`.
 
Common combinations:
 
- **Building a 3D scene**: threejs-fundamentals (primary) + threejs-geometry + threejs-materials + threejs-lighting
- **Interactive 3D experience**: threejs-fundamentals + threejs-interaction (primary) + threejs-animation + threejs-materials
- **Visual effects and shaders**: threejs-shader-forge (primary) + glsl-shader-alchemist + threejs-postprocessing + threejs-materials
- **Loading external models**: threejs-loaders (primary) + threejs-materials + threejs-lighting + threejs-animation
- **Generative art**: algorithmic-art (primary) + glsl-shader-alchemist + threejs-postprocessing
- **Makepad UI animations**: makepad-animator (primary) + makepad-shader-lab
- **Spline integration**: spline-3d-integration (primary) + threejs-fundamentals
- **Scroll-driven effects**: scroll-experience (primary) + threejs-fundamentals + threejs-animation
 
## Package Structure
 
- `SKILL.md` — lightweight router and high-level index
- `composition-protocol.md` — universal rules for selecting and combining mini-skills
- `self-diagnostic-protocol.md` — self-diagnostic rules for this domain package
- `resources/skill-catalog.md` — full catalog of extracted mini-skills
- `resources/routing-guide.md` — navigation and composition rules
- `resources/asset-link-index.md` — complete link map for every auxiliary folder and file
- `resources/manifest.json` — machine-readable package manifest
- `references/skills/*.md` — full extracted guidance per mini-skill
- `examples/skills/*.md` — extracted code snippets and usage samples
 
## Mini-Skills Index
 
### algorithmic-art
- Summary: Create generative art using p5.js with seeded randomness, algorithmic philosophies, and interactive parameter controls.
- Open reference: `references/skills/algorithmic-art.md`
- Open examples: `examples/skills/algorithmic-art.md`
 
### makepad-animator
- Summary: Implement Makepad animation states and transitions with forward timing, snap changes, and shader uniform animation.
- Open reference: `references/skills/makepad-animator.md`
- Open examples: `examples/skills/makepad-animator.md`
 
### makepad-shader-lab
- Summary: Write Makepad custom pixel shaders using Sdf2d, uniforms, gradients, and rounded-box rendering.
- Open reference: `references/skills/makepad-shader-lab.md`
- Open examples: `examples/skills/makepad-shader-lab.md`
 
### scroll-experience
- Summary: Build scroll-driven web animations using GSAP ScrollTrigger, Framer Motion, Locomotive Scroll, Lenis, and CSS scroll-timeline.
- Open reference: `references/skills/scroll-experience.md`
- Open examples: `examples/skills/scroll-experience.md`
 
### glsl-shader-alchemist
- Summary: Write GPU shaders using GLSL for WebGL, Three.js, or game engines, covering vertex and fragment shaders, uniforms, and vector math.
- Open reference: `references/skills/glsl-shader-alchemist.md`
- Open examples: `examples/skills/glsl-shader-alchemist.md`
 
### spline-3d-integration
- Summary: Embed interactive 3D scenes from Spline.design into web projects with vanilla JS, React, Next.js, and Vue integration.
- Open reference: `references/skills/spline-3d-integration.md`
- Open examples: `examples/skills/spline-3d-integration.md`
 
### threejs-animation
- Summary: Implement Three.js procedural and keyframe animation using Timer, AnimationClip, AnimationMixer, and AnimationAction.
- Open reference: `references/skills/threejs-animation.md`
- Open examples: `examples/skills/threejs-animation.md`
 
### threejs-fundamentals
- Summary: Set up Three.js core infrastructure including scene, camera, renderer, fog, import maps, responsive resize, and animation loop.
- Open reference: `references/skills/threejs-fundamentals.md`
- Open examples: `examples/skills/threejs-fundamentals.md`
 
### threejs-geometry
- Summary: Work with Three.js built-in geometries, custom BufferGeometry, instanced meshes, and geometry merging.
- Open reference: `references/skills/threejs-geometry.md`
- Open examples: `examples/skills/threejs-geometry.md`
 
### threejs-interaction
- Summary: Implement Three.js user interaction with OrbitControls, raycasting, mouse picking, and click detection.
- Open reference: `references/skills/threejs-interaction.md`
- Open examples: `examples/skills/threejs-interaction.md`
 
### threejs-lighting
- Summary: Configure Three.js lighting systems including ambient, directional, hemisphere, point, and spot lights with shadow mapping.
- Open reference: `references/skills/threejs-lighting.md`
- Open examples: `examples/skills/threejs-lighting.md`
 
### threejs-loaders
- Summary: Load external assets in Three.js using GLTFLoader, TextureLoader, LoadingManager, and model post-processing.
- Open reference: `references/skills/threejs-loaders.md`
- Open examples: `examples/skills/threejs-loaders.md`
 
### threejs-materials
- Summary: Work with Three.js material types including MeshBasicMaterial, MeshLambertMaterial, MeshStandardMaterial, and PBR workflows.
- Open reference: `references/skills/threejs-materials.md`
- Open examples: `examples/skills/threejs-materials.md`
 
### threejs-postprocessing
- Summary: Apply Three.js post-processing effects using EffectComposer, RenderPass, UnrealBloomPass, and custom shader passes.
- Open reference: `references/skills/threejs-postprocessing.md`
- Open examples: `examples/skills/threejs-postprocessing.md`
 
### threejs-shader-forge
- Summary: Create custom Three.js ShaderMaterial and RawShaderMaterial with GLSL vertex and fragment shaders, uniforms, and TSL NodeMaterial.
- Open reference: `references/skills/threejs-shader-forge.md`
- Open examples: `examples/skills/threejs-shader-forge.md`
 
### threejs-textures
- Summary: Load, configure, and optimize textures in Three.js including async loading, mipmaps, compression, and texture atlases.
- Open reference: `references/skills/threejs-textures.md`
- Open examples: `examples/skills/threejs-textures.md`
 
## Validation
 
- Keep detailed implementation guidance outside the main `SKILL.md`.
- Prefer adding or updating auxiliary files rather than re-expanding the router.
- Preserve skill-specific constraints, examples, and workflow details in the extracted files.
 
## Output Requirements
 
- Keep the main file concise and navigational.
- Store deep guidance in auxiliary files.
- Use descriptive, stable file names for extracted mini-skills.
