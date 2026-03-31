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
