---
name: "threejs-lighting"
title: "Three.js Lighting"
description: "Use for configuring Three.js lighting systems including ambient, directional, hemisphere, point, and spot lights with shadow mapping."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-lighting.md`
- Examples: `examples/skills/threejs-lighting.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for scene setup
- Adjacent: `references/skills/threejs-materials.md` — for material-light interaction
- Validation: `references/skills/threejs-postprocessing.md` — for lighting-related effects

## Purpose

Configure lighting in Three.js scenes. Covers all light types, shadow mapping, environment maps, and performance optimization for lit scenes.

## When to Use

- When adding or configuring lights in a Three.js scene
- When implementing shadows
- When setting up environment maps for PBR materials
- When optimizing scene lighting for performance

## Workflow

1. Start with ambient or hemisphere light for base illumination.
2. Add directional light for primary lighting (sunlight-like).
3. Add point or spot lights for localized illumination.
4. Enable shadows on renderer and configure shadow-casting lights.
5. Set shadow map size and frustum for quality-performance balance.
6. Use light layers to exclude objects from specific lights.

## Quality Standards

- Limit light count — each light adds shader complexity.
- Use baked lighting for static scenes.
- Use shadow maps of 512–1024 for most cases.
- Keep shadow camera frustums tight to cover only the needed area.
- Disable shadows on lights that do not need them.

## Technical Rules

Light types: AmbientLight (uniform, no shadows), HemisphereLight (sky + ground, no shadows), DirectionalLight (parallel rays, supports shadows), PointLight (omnidirectional, supports shadows), SpotLight (cone, supports shadows), RectAreaLight (rectangular, no shadows).

Shadow setup: enable `renderer.shadowMap.enabled = true`, set `light.castShadow = true`, configure `light.shadow.mapSize`, set `mesh.castShadow` and `mesh.receiveShadow`.

## Validation

- Verify all lights illuminate the scene as expected.
- Check shadow quality and coverage.
- Confirm performance stays at 60fps with all lights active.
- Test with different material types.

## Restrictions

- Do not use more shadow-casting lights than necessary.
- Do not set shadow map sizes above 2048 without profiling.
- Do not skip testing light interaction with materials.

## Output Requirements

- Complete lighting setup with ambient and directional lights at minimum.
- Shadow configuration when shadows are needed.
- Comments explaining light parameters and their visual effect.
