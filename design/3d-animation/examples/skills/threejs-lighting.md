# Three.js Lighting — Examples

## Basic Lighting Setup

```javascript
import * as THREE from "three";

const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);
scene.add(directionalLight);
```

## Ambient Light

```javascript
const ambient = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambient);

// Modify at runtime
ambient.color.set(0xffffcc);
ambient.intensity = 0.3;
```

## Hemisphere Light

```javascript
const hemi = new THREE.HemisphereLight(0x87ceeb, 0x8b4513, 0.6);
hemi.position.set(0, 50, 0);
scene.add(hemi);

// Properties
hemi.color;       // Sky color
hemi.groundColor; // Ground color
hemi.intensity;
```

## Performance Tips

1. Limit light count — each light adds shader complexity.
2. Use baked lighting for static scenes.
3. Use shadow maps of 512–1024 for most cases.
4. Keep shadow camera frustums tight.
5. Disable shadows on lights that do not need them.
6. Use light layers to exclude objects from certain lights.

## Shadow Quality / Performance Triage Example

### Before / After Shadow Settings

| Setting | Before | After |
|---|---|---|
| shadow map size | 4096 | 2048 desktop / 1024 mobile |
| PCF mode | PCFSoft | PCFSoft desktop, Basic mobile |
| light count with shadows | 3 | 1 key + baked fill |

### Shadow Map Budget Table

| Tier | Max Shadow Maps | Max Total Resolution |
|---|---:|---:|
| Desktop | 2 | 4096^2 combined |
| Mobile | 1 | 1024^2 |

### Mobile Fallback
- Disable contact shadows and lower shadow camera frustum updates.

### Visual QA Gates
- No peter-panning on hero assets.
- Penumbra softness consistent across camera orbit.
- Frame time impact from shadows <= 4ms on baseline desktop.

