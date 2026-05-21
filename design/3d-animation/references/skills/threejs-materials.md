---
name: "threejs-materials"
title: "Three.js Materials"
description: "Use for working with Three.js material types including MeshBasicMaterial, MeshLambertMaterial, MeshStandardMaterial, and PBR workflows."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-materials.md`
- Examples: `examples/skills/threejs-materials.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-textures.md` — for texture maps (color, normal, roughness)
- Adjacent: `references/skills/threejs-lighting.md` — for light-material interaction
- Validation: `references/skills/threejs-fundamentals.md` — for rendering context

## Purpose

Select, configure, and optimize materials for Three.js meshes. Covers the full material hierarchy from basic unlit materials to physically-based rendering (PBR) with MeshStandardMaterial and MeshPhysicalMaterial.

## When to Use

- When choosing the right material type for a mesh
- When configuring PBR properties (roughness, metalness, env maps)
- When working with transparency, alpha testing, or double-sided rendering
- When optimizing material performance for complex scenes

## Workflow

1. Choose material type based on needs: Basic (unlit), Lambert (diffuse), Phong (specular), Standard (PBR), Physical (advanced PBR).
2. Configure base properties: color, opacity, side, wireframe.
3. Apply texture maps if needed: map, normalMap, roughnessMap, metalnessMap, envMap.
4. Set PBR properties for Standard/Physical: roughness, metalness, clearcoat, transmission.
5. Optimize: reuse materials, prefer simpler types when possible, use alphaTest over transparency.

## Quality Standards

- Reuse materials — same material instance enables batched draw calls.
- Avoid transparent materials when possible — they require sorting.
- Use alphaTest instead of full transparency when applicable.
- Choose the simplest material that achieves the visual goal: Basic > Lambert > Phong > Standard > Physical.
- Limit active lights — each adds shader complexity to lit materials.

## Technical Rules

Material hierarchy (simplest to most complex):
- `MeshBasicMaterial`: unlit, no light response. Properties: color, map, envMap, opacity, transparent, side, wireframe.
- `MeshLambertMaterial`: diffuse shading. Adds: emissive, emissiveMap, emissiveIntensity.
- `MeshPhongMaterial`: specular highlights. Adds: specular, shininess, specularMap.
- `MeshStandardMaterial`: PBR. Adds: roughness, metalness, roughnessMap, metalnessMap.
- `MeshPhysicalMaterial`: advanced PBR. Adds: clearcoat, transmission, thickness, ior, sheen.

Common properties: `side` (FrontSide, BackSide, DoubleSide), `transparent`, `opacity`, `alphaMap`, `fog`, `depthTest`, `depthWrite`.

## Validation

- Verify material appears correctly with the scene lighting.
- Check transparency and depth sorting.
- Confirm PBR materials respond to environment maps.
- Test material disposal when removing meshes.

## Restrictions

- Do not use MeshPhysicalMaterial when MeshStandardMaterial suffices.
- Do not enable transparency without testing depth sorting.
- Do not forget `material.needsUpdate = true` after changing texture references at runtime.

## Output Requirements

- Material configuration with all relevant properties.
- Texture map assignments when applicable.
- Comments explaining material choice rationale.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Material Review Failure Modes
- Wrong material class selected for intended lighting model.
- PBR maps missing or misassigned (normal/roughness/metalness/ao).
- Transparent objects render in wrong order with depth artifacts.
- Color-space mismatch between albedo and data maps.
- Roughness/normal values overly aggressive and break realism.
- Texture-heavy materials exceed frame/memory budgets.

### Diagnostics Workflow (Material Quality)
1. Validate material selection against object function (hero, UI 3D, background).
2. Run PBR map checklist for channel correctness and UV usage.
3. Inspect transparent assets with renderOrder/depthWrite permutations.
4. Audit color-space settings for all bound textures.
5. Compare visual/perf tradeoffs between high-fidelity and fallback materials.

### Evidence Required
- Material property before/after table for corrected assets.
- Map validation checklist (present, colorSpace, channel correctness).
- Transparent-object note documenting renderOrder and depthWrite decisions.

### Acceptance Gates
- Materials match art direction under target lighting setup.
- Transparency artifacts eliminated in primary camera paths.
- Material stack remains within performance and memory targets.

### Validation Neighbors
- `threejs-textures` for map payload and color-space correctness.
- `threejs-lighting` for physically based response validation.
- `procedural-shader-debugging` for shader-driven material anomalies.

