# Three.js Interaction — Examples

## OrbitControls + Raycasting

```javascript
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

function onClick(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(scene.children);

  if (intersects.length > 0) {
    console.log("Clicked:", intersects[0].object);
  }
}

window.addEventListener("click", onClick);
```

## Raycaster API

```javascript
const raycaster = new THREE.Raycaster();

// From camera (mouse picking)
raycaster.setFromCamera(mousePosition, camera);

// From any origin and direction
raycaster.set(origin, direction); // origin: Vector3, direction: normalized Vector3

// Get intersections
const intersects = raycaster.intersectObjects(objects, recursive);

// Intersection data:
// { distance, point (Vector3), face, faceIndex, object, uv, normal, instanceId }
```

## Mouse NDC Conversion

```javascript
const mouse = new THREE.Vector2();

// For full window
function updateMouse(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
}

// For specific canvas element
function updateMouseCanvas(event, canvas) {
  const rect = canvas.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
}
```

## Performance Tips

1. Throttle mousemove handlers to limit raycasts.
2. Use layers to filter raycast targets.
3. Use simple collision meshes for complex geometry.
4. Disable controls when not needed: `controls.enabled = false`.
5. Batch interaction checks.

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

