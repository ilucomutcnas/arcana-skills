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

## Texture Memory Reduction Plan Example

### Before / After Texture Budget

| Asset Group | Before MB | After MB | Strategy |
|---|---:|---:|---|
| Hero albedo set | 96 | 36 | atlas + KTX2 |
| Normal/ORM set | 64 | 28 | resolution tiering |
| UI decals | 22 | 8 | sprite atlas reuse |

### Rules
- Enable mipmaps for minified textures.
- Limit anisotropy to device-supported cap with project max (often 4-8).
- Set `colorSpace` correctly (sRGB for color maps, linear for data maps).

### Atlas Strategy
- Merge small props into shared atlas to cut texture binds.

### Async Loading / Disposal Snippet

```javascript
const tex = await textureLoader.loadAsync(url);
tex.colorSpace = THREE.SRGBColorSpace;
// ... later on teardown
tex.dispose();
```

### Compression Notes
- Prefer KTX2/Basis pipeline in build stage; DRACO handles geometry, not texture payload.

