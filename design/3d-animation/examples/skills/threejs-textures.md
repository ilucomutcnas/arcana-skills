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
