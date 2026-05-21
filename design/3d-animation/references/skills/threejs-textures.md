---
name: "threejs-textures"
title: "Three.js Textures"
description: "Use for loading, configuring, and optimizing textures in Three.js including async loading, mipmaps, compression, and texture atlases."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-textures.md`
- Examples: `examples/skills/threejs-textures.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-materials.md` — for applying textures to materials
- Adjacent: `references/skills/threejs-loaders.md` — for asset loading patterns
- Validation: `references/skills/threejs-fundamentals.md` — for rendering context

## Purpose

Load, configure, and optimize textures for Three.js materials. Covers TextureLoader, async loading patterns, texture properties (wrapping, filtering, mipmaps), compression formats, and performance best practices.

## When to Use

- When loading image textures for materials
- When configuring texture wrapping, filtering, or repeat
- When optimizing texture memory and bandwidth
- When loading multiple textures asynchronously

## Workflow

1. Use power-of-2 dimensions for textures: 256, 512, 1024, 2048.
2. Compress textures with KTX2/Basis for web delivery.
3. Use texture atlases to reduce texture switches.
4. Enable mipmaps for objects viewed at varying distances.
5. Limit texture size — 2048 is usually sufficient for web.
6. Reuse texture instances — same texture = better batching.

## Quality Standards

- Use power-of-2 dimensions for all textures.
- Compress textures for web delivery.
- Enable mipmaps for distant objects.
- Reuse texture instances across materials.
- Limit maximum texture resolution to 2048 for most web use cases.

## Technical Rules

- `THREE.TextureLoader.load(url, onLoad, onProgress, onError)`: loads image textures.
- Async pattern: wrap in Promise for `await` usage.
- Texture properties: `wrapS`, `wrapT` (RepeatWrapping, ClampToEdgeWrapping, MirroredRepeatWrapping), `repeat`, `offset`, `minFilter`, `magFilter`.
- Set `texture.needsUpdate = true` after changing properties at runtime.
- Dispose textures when no longer needed: `texture.dispose()`.

## Validation

- Verify textures load and display correctly on materials.
- Check texture dimensions are power-of-2 for mipmap support.
- Confirm async loading handles errors gracefully.
- Test texture memory usage on target devices.

## Restrictions

- Do not use non-power-of-2 textures with mipmap filtering.
- Do not forget to dispose textures when removing objects.
- Do not load oversized textures for web delivery without compression.

## Output Requirements

- Complete texture loading code with error handling.
- Texture configuration for wrapping and filtering.
- Async loading patterns when loading multiple textures.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Production Failure Modes
- Texture memory footprint exceeds per-tier GPU budget.
- Mipmap generation is incorrect for NPOT or UI-critical assets.
- Anisotropy is set above practical device caps.
- `colorSpace` assignments are inconsistent across albedo/data textures.
- KTX2/DRACO asset references are misaligned with loader capabilities (without new binaries).
- Atlas strategy introduces bleeding or UV mismatch.
- Async texture loads race scene readiness and display placeholders indefinitely.
- Disposal lifecycle misses texture cleanup on route changes.

### Diagnostics Workflow (Three.js Textures)
1. Inventory texture formats/resolutions and compare against tiered memory budget.
2. Validate mipmap policy per texture type and NPOT constraints.
3. Cap anisotropy by queried device maximum and project budget ceiling.
4. Audit colorSpace rules for color vs data maps.
5. Verify KTX2/DRACO reference paths and runtime fallback behavior without bundling binaries here.
6. Test atlas edges under minification to catch bleeding artifacts.
7. Confirm async loading states and final bind timing for all critical textures.
8. Execute disposal audit for texture and loader lifecycles.

### Release Evidence Format
- Before/after texture memory table by asset group and device tier.
- Texture settings checklist (mipmaps, anisotropy, wrap/filter, colorSpace).
- Disposal/loader lifecycle note summarizing creation, bind, release, and cache policy.

### Acceptance / Rejection Criteria
- **Accept** when memory usage and quality targets are both satisfied per tier.
- **Reject** if colorSpace misconfiguration causes visible color drift.
- **Reject** when async load races can leave unresolved placeholders.
- **Accept** only when disposal and cache policy prevent texture leaks.

### Adjacent Mini-Skills to Use for Validation
- `threejs-materials`
- `threejs-loaders`
- `threejs-fundamentals`
