# Three.js Loaders — Examples

## Basic GLTF Loading

```javascript
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

const loader = new GLTFLoader();
loader.load("model.glb", (gltf) => {
  scene.add(gltf.scene);
});

const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load("texture.jpg");
```

## Model Post-Processing

```javascript
loader.load("model.glb", (gltf) => {
  const model = gltf.scene;

  // Enable shadows
  model.traverse((child) => {
    if (child.isMesh) {
      child.castShadow = true;
      child.receiveShadow = true;
    }
  });

  // Find specific mesh
  const head = model.getObjectByName("Head");

  // Adjust materials
  model.traverse((child) => {
    if (child.isMesh && child.material) {
      child.material.envMapIntensity = 0.5;
    }
  });

  // Center and scale
  const box = new THREE.Box3().setFromObject(model);
  const center = box.getCenter(new THREE.Vector3());
  const size = box.getSize(new THREE.Vector3());

  model.position.sub(center);
  const maxDim = Math.max(size.x, size.y, size.z);
  model.scale.setScalar(1 / maxDim);

  scene.add(model);
});
```

## Loading Manager

```javascript
const manager = new THREE.LoadingManager();

manager.onStart = (url, loaded, total) => {
  console.log(`Started loading: ${url}`);
};

manager.onLoad = () => {
  console.log("All assets loaded!");
  startGame();
};

manager.onProgress = (url, loaded, total) => {
  const progress = (loaded / total) * 100;
  console.log(`Loading: ${progress.toFixed(1)}%`);
  updateProgressBar(progress);
};

manager.onError = (url) => {
  console.error(`Error loading: ${url}`);
};

const textureLoader = new THREE.TextureLoader(manager);
const gltfLoader = new GLTFLoader(manager);

textureLoader.load("texture1.jpg");
textureLoader.load("texture2.jpg");
gltfLoader.load("model.glb");
// manager.onLoad fires when ALL are complete
```

## Texture Loading with Callbacks

```javascript
const loader = new THREE.TextureLoader();

loader.load(
  "texture.jpg",
  (texture) => {
    material.map = texture;
    material.needsUpdate = true;
  },
  undefined,
  (error) => {
    console.error("Error loading texture", error);
  },
);
```

## Model Loading Pipeline Release Example

### LoadingManager States
- `onStart`: show skeleton placeholder.
- `onProgress`: update determinate progress bar.
- `onError`: switch to fallback poster/model + retry CTA.
- `onLoad`: hide loader and emit analytics success event.

### Fallback Behavior
- Prefer low-poly proxy GLB when primary fails.
- If both fail, keep static poster and textual feature summary.

### Cancellation / Caching Notes
- Abort in-flight fetch when route changes.
- Cache successfully parsed assets by URL + version key.

### GLTF Transform Checklist
- [ ] Normalize scale and center pivot.
- [ ] Validate material assignments and tangents.
- [ ] Strip unused animation clips.

### Release Checklist
- [ ] Offline/error path tested.
- [ ] Progress UI does not stall at 99%.
- [ ] Fallback path maintains layout height.

