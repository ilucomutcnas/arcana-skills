# Three.js Geometry — Examples

## Basic Geometry Creation

```javascript
import * as THREE from "three";

const box = new THREE.BoxGeometry(1, 1, 1);
const sphere = new THREE.SphereGeometry(0.5, 32, 32);
const plane = new THREE.PlaneGeometry(10, 10);

const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
const mesh = new THREE.Mesh(box, material);
scene.add(mesh);
```

## All Built-In Geometries

```javascript
// Box — width, height, depth, widthSegments, heightSegments, depthSegments
new THREE.BoxGeometry(1, 1, 1, 1, 1, 1);

// Sphere — radius, widthSegments, heightSegments, phiStart, phiLength, thetaStart, thetaLength
new THREE.SphereGeometry(1, 32, 32);
new THREE.SphereGeometry(1, 32, 32, 0, Math.PI); // Hemisphere

// Plane — width, height, widthSegments, heightSegments
new THREE.PlaneGeometry(10, 10, 1, 1);

// Circle — radius, segments, thetaStart, thetaLength
new THREE.CircleGeometry(1, 32);

// Cylinder — radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded
new THREE.CylinderGeometry(1, 1, 2, 32, 1, false);
new THREE.CylinderGeometry(0, 1, 2, 32); // Cone shape
new THREE.CylinderGeometry(1, 1, 2, 6);  // Hexagonal prism

// Cone — radius, height, radialSegments, heightSegments, openEnded
new THREE.ConeGeometry(1, 2, 32, 1, false);

// Torus — radius, tube, radialSegments, tubularSegments, arc
new THREE.TorusGeometry(1, 0.4, 16, 100);

// TorusKnot — radius, tube, tubularSegments, radialSegments, p, q
new THREE.TorusKnotGeometry(1, 0.4, 100, 16, 2, 3);

// Ring — innerRadius, outerRadius, thetaSegments, phiSegments
new THREE.RingGeometry(0.5, 1, 32, 1);

// Capsule — radius, length, capSegments, radialSegments (r142+)
new THREE.CapsuleGeometry(0.5, 1, 4, 8);

// Platonic solids
new THREE.DodecahedronGeometry(1, 0);
new THREE.IcosahedronGeometry(1, 0);
new THREE.OctahedronGeometry(1, 0);
new THREE.TetrahedronGeometry(1, 0);

// Custom polyhedron — vertices, indices, radius, detail
const vertices = [1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1];
const indices = [2, 1, 0, 0, 3, 2, 1, 3, 0, 2, 3, 1];
new THREE.PolyhedronGeometry(vertices, indices, 1, 0);
```

## Performance Tips

1. Use indexed geometry: reuse vertices with indices.
2. Merge static meshes: reduce draw calls with `mergeGeometries`.
3. Use `InstancedMesh`: for many identical objects.
4. Choose appropriate segment counts: more segments = smoother but slower.
5. Dispose unused geometry: `geometry.dispose()`.
