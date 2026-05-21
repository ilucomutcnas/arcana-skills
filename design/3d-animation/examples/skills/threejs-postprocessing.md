# Three.js Post-Processing — Examples

## Basic Bloom Setup

```javascript
import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";

const composer = new EffectComposer(renderer);

const renderPass = new RenderPass(scene, camera);
composer.addPass(renderPass);

const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5,  // strength
  0.4,  // radius
  0.85, // threshold
);
composer.addPass(bloomPass);

function animate() {
  requestAnimationFrame(animate);
  composer.render(); // NOT renderer.render()
}
```

## Composer with Resize Handling

```javascript
const composer = new EffectComposer(renderer);

const renderPass = new RenderPass(scene, camera);
composer.addPass(renderPass);

composer.addPass(effectPass);

effectPass.renderToScreen = true; // Default for last pass

function onResize() {
  const width = window.innerWidth;
  const height = window.innerHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();

  renderer.setSize(width, height);
  composer.setSize(width, height);
}
```

## Bloom Runtime Adjustment

```javascript
const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5, 0.4, 0.85,
);
composer.addPass(bloomPass);

// Adjust at runtime
bloomPass.strength = 2.0;
bloomPass.threshold = 0.5;
bloomPass.radius = 0.8;
```

## Performance Tips

1. Limit passes — each adds a full-screen render.
2. Lower resolution for blur passes.
3. Disable unused effects: `pass.enabled = false`.
4. Use FXAA over MSAA — less expensive anti-aliasing.
5. Profile with DevTools — check GPU usage.

## Bloom Regression Triage Example

### Pass Ordering Table

| Order | Pass | Reason |
|---:|---|---|
| 1 | RenderPass | base scene color/depth |
| 2 | custom edge pass | generate edge mask pre-bloom |
| 3 | UnrealBloomPass | glow on HDR highlights |
| 4 | OutputPass | final tone mapping |

### Render Target / DPR Budget
- Composer size must track renderer size and DPR cap.
- Cap DPR to 1.5 when bloom enabled on mobile.

### Mobile Disable Path
- Disable bloom + custom pass when GPU tier low or reduced motion/data saver enabled.

### Before / After Composer Snippet

```javascript
// Before: bloom before custom pass caused clipping
composer.addPass(bloomPass);
composer.addPass(edgePass);

// After
composer.addPass(edgePass);
composer.addPass(bloomPass);
```

### QA Gates
- No highlight clipping at exposure sweep 0.8-1.4.
- Post stack cost <= 6ms desktop baseline.

