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
