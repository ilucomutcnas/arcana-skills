# Three.js Materials — Examples

## PBR Material (Recommended)

```javascript
import * as THREE from "three";

const material = new THREE.MeshStandardMaterial({
  color: 0x00ff00,
  roughness: 0.5,
  metalness: 0.5,
});

const mesh = new THREE.Mesh(geometry, material);
```

## Basic Material (Unlit)

```javascript
const material = new THREE.MeshBasicMaterial({
  color: 0xff0000,
  transparent: true,
  opacity: 0.5,
  side: THREE.DoubleSide,
  wireframe: false,
  map: texture,
  alphaMap: alphaTexture,
  envMap: envTexture,
  reflectivity: 1,
  fog: true,
});
```

## Lambert Material (Diffuse)

```javascript
const material = new THREE.MeshLambertMaterial({
  color: 0x00ff00,
  emissive: 0x111111,
  emissiveIntensity: 1,
  map: texture,
  emissiveMap: emissiveTexture,
  envMap: envTexture,
  reflectivity: 0.5,
});
```

## Material Hierarchy (Simplest to Most Complex)

1. `MeshBasicMaterial` — unlit, no light response
2. `MeshLambertMaterial` — diffuse shading
3. `MeshPhongMaterial` — specular highlights
4. `MeshStandardMaterial` — PBR (roughness + metalness)
5. `MeshPhysicalMaterial` — advanced PBR (clearcoat, transmission, sheen)

## Performance Tips

1. Reuse materials — same material = batched draw calls.
2. Avoid transparent when possible — requires sorting.
3. Use alphaTest instead of transparency when applicable.
4. Choose simpler materials when visual quality allows.
5. Limit active lights — each adds shader complexity.

## Production Evidence Addendum

### Constraints
- Frame budget target: <= 16.6ms on desktop baseline, <= 25ms on mid-range mobile fallback path.
- Regression threshold: reject if draw calls or GPU memory increase > 15% without approval.
- Accessibility gate: reduced-motion path and non-pointer interaction fallback must be validated.

### Release Checks
1. Deterministic reproduction steps documented with exact parameter/state values.
2. Browser matrix logged (Chrome + Safari + Firefox + one mobile browser).
3. Before/after screenshots or metric notes recorded in PR description (no binary assets required in repository).
4. Rollback switch documented (feature flag, material fallback, or effect disable path).

