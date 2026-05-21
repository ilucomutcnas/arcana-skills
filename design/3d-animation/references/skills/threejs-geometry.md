---
name: "threejs-geometry"
title: "Three.js Geometry"
description: "Use for working with Three.js built-in geometries, custom BufferGeometry, instanced meshes, and geometry merging."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/threejs-geometry.md`
- Examples: `examples/skills/threejs-geometry.md`

## Linked Package Files

- Adjacent: `references/skills/threejs-fundamentals.md` — for scene setup
- Adjacent: `references/skills/threejs-materials.md` — for material pairing
- Validation: `references/skills/threejs-interaction.md` — for raycasting on geometry

## Purpose

Work with Three.js geometry types: built-in parametric geometries, custom BufferGeometry, instanced meshes for high-performance rendering, and geometry merging for draw call optimization.

## When to Use

- When creating 3D shapes using built-in geometries (box, sphere, plane, torus, etc.)
- When building custom geometry from vertices and indices
- When optimizing many identical objects with InstancedMesh
- When merging static geometries to reduce draw calls

## Workflow

1. Choose the appropriate built-in geometry or create custom BufferGeometry.
2. Set segment counts appropriately — more segments = smoother but slower.
3. Use indexed geometry to reuse vertices.
4. For many identical objects, use `THREE.InstancedMesh`.
5. For static objects, merge geometries with `mergeGeometries`.
6. Dispose unused geometry with `geometry.dispose()`.

## Quality Standards

- Use indexed geometry for vertex reuse.
- Merge static meshes to reduce draw calls.
- Use InstancedMesh for many identical objects.
- Choose appropriate segment counts for the viewing distance.
- Always dispose geometry that is no longer needed.

## Technical Rules

Built-in geometries: BoxGeometry, SphereGeometry, PlaneGeometry, CircleGeometry, CylinderGeometry, ConeGeometry, TorusGeometry, TorusKnotGeometry, RingGeometry, CapsuleGeometry (r142+), DodecahedronGeometry, IcosahedronGeometry, OctahedronGeometry, TetrahedronGeometry, PolyhedronGeometry.

Custom geometry: use `THREE.BufferGeometry` with `Float32BufferAttribute` for positions, normals, and UVs.

Do not use `THREE.CapsuleGeometry` in Three.js versions before r142.

## Validation

- Verify geometry renders correctly with appropriate materials.
- Check that custom geometry has correct normals for lighting.
- Confirm instanced meshes display all instances.
- Test geometry disposal does not cause memory leaks.

## Restrictions

- Do not use deprecated `THREE.Geometry` — always use `THREE.BufferGeometry`.
- Do not use `THREE.CapsuleGeometry` before r142.
- Do not forget to dispose geometry when removing objects.

## Output Requirements

- Complete geometry creation code with appropriate parameters.
- Include material pairing for visual testing.
- Document segment counts and their visual impact.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Production Failure Modes
- Draw-call count exceeds scene budget due to over-fragmented meshes.
- BufferGeometry attributes contain mismatched lengths or invalid boundaries.
- InstancedMesh is skipped where repeated meshes dominate scene cost.
- Merge strategy removes needed per-part transforms or materials.
- Bounding volumes are stale, breaking culling and interaction accuracy.
- Normals/tangents are invalid, causing shading seams.
- Geometry disposal is incomplete on scene replacement.

### Diagnostics Workflow (Three.js Geometry)
1. Capture baseline draw calls and identify top geometry contributors.
2. Validate every BufferGeometry attribute count and index bounds before upload.
3. Apply InstancedMesh decision rules for repeated assets and compare CPU/GPU cost.
4. Evaluate merge candidates while preserving material groups and transforms.
5. Recompute and verify bounding sphere/box after procedural or loader-side edits.
6. Run normal/tangent integrity checks for PBR-ready shading.
7. Confirm `geometry.dispose()` coverage during teardown.

### Release Evidence Format
- Draw-call before/after table by scene checkpoint.
- Memory table including geometry count, vertex count, and GPU memory estimate.
- Bounding volume validation notes for culling and picking correctness.

### Acceptance / Rejection Criteria
- **Accept** when draw calls are within documented budget and visual output is unchanged.
- **Reject** if merged or instanced paths break material assignment or transforms.
- **Reject** when bounding volumes are stale and cause missed picks or over-culling.
- **Accept** only when disposal checklist confirms no orphan geometries.

### Adjacent Mini-Skills to Use for Validation
- `threejs-materials`
- `threejs-fundamentals`
- `threejs-loaders`
