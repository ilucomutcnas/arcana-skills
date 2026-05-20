# Three.js Textures — Examples

## Basic Texture Loading

```javascript
import * as THREE from "three";

const loader = new THREE.TextureLoader();
const texture = loader.load("texture.jpg");

const material = new THREE.MeshStandardMaterial({
  map: texture,
});
```

## Async Loading with Callbacks

```javascript
const loader = new THREE.TextureLoader();

loader.load(
  "texture.jpg",
  (texture) => console.log("Loaded"),
  (progress) => console.log("Progress"),
  (error) => console.error("Error"),
);

// Synchronous style (loads async internally)
const texture = loader.load("texture.jpg");
material.map = texture;
```

## Promise-Based Loading

```javascript
function loadTexture(url) {
  return new Promise((resolve, reject) => {
    new THREE.TextureLoader().load(url, resolve, undefined, reject);
  });
}

const [colorMap, normalMap, roughnessMap] = await Promise.all([
  loadTexture("color.jpg"),
  loadTexture("normal.jpg"),
  loadTexture("roughness.jpg"),
]);
```

## Optimization Rules

1. Use power-of-2 dimensions: 256, 512, 1024, 2048.
2. Compress textures: KTX2/Basis for web delivery.
3. Use texture atlases: reduce texture switches.
4. Enable mipmaps: for distant objects.
5. Limit texture size: 2048 usually sufficient for web.
6. Reuse textures: same texture = better batching.

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

