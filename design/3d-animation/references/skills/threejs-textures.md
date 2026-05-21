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

### Texture Pipeline Failure Modes
- Aggregate texture memory exceeds budget on mid-tier devices.
- Missing mipmaps causes shimmering at distance.
- Unbounded anisotropy increases sampling cost with limited visual gain.
- Incorrect colorSpace assignment distorts albedo or data maps.
- Compression strategy unclear (KTX2 for textures vs DRACO for geometry).
- Async loader lifecycle leaks textures after scene disposal.
- Atlas packing introduces UV bleed if padding rules are ignored.

### Diagnostics Workflow (Texture Governance)
1. Inventory texture set and compute memory footprint by asset group.
2. Verify mipmap generation and min/mag filters for each critical map.
3. Set anisotropy caps by device tier and compare quality/perf impact.
4. Audit colorSpace assignments (sRGB vs linear) map-by-map.
5. Validate atlas packing with UV edge test patterns.
6. Trace async load/dispose lifecycle to ensure textures are released.

### Release Evidence Format
- Before/after texture memory table.
- Texture settings checklist (mipmaps, anisotropy, colorSpace, compression flag).
- Loader/disposal lifecycle note describing when textures are freed.

### Acceptance Gates
- Texture memory remains within defined platform budgets.
- No visible shimmer/bleed artifacts in standard camera paths.
- Disposal verified: no persistent GPU texture growth after scene teardown.

### Validation Neighbors
- `threejs-materials` for map usage and shading output.
- `threejs-loaders` for async delivery and fallback behavior.
- `threejs-fundamentals` for renderer color and lifecycle consistency.

