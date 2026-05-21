# GLSL Shader Alchemist — Examples

## Basic Vertex Shader

```glsl
attribute vec3 position;
uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;

void main() {
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

## Basic Fragment Shader

```glsl
uniform vec3 color;

void main() {
    gl_FragColor = vec4(color, 1.0);
}
```

## Passing UV Coordinates

```glsl
// Vertex Shader
varying vec2 vUv;

void main() {
    vUv = uv;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

```glsl
// Fragment Shader
varying vec2 vUv;

void main() {
    // Gradient based on UV
    gl_FragColor = vec4(vUv.x, vUv.y, 1.0, 1.0);
}
```

## Key GLSL Functions

- `mix(a, b, t)` — linear interpolation
- `step(edge, x)` — hard threshold (returns 0.0 or 1.0)
- `smoothstep(edge0, edge1, x)` — smooth threshold
- `clamp(x, min, max)` — constrain range
- `fract(x)` — fractional part
- `length(v)` — vector magnitude
- `normalize(v)` — unit vector
- `dot(a, b)` — dot product
- `cross(a, b)` — cross product (vec3 only)
- `reflect(I, N)` — reflection vector

## Performance Tips

- Use `mix()` instead of `if-else` for conditional coloring.
- Use `step()` and `smoothstep()` instead of branching.
- Pack data into `vec4` to minimize memory access.
- Pre-calculate constant values on the CPU as uniforms.

## Fragment Shader Release Example

### Uniform Table

| Uniform | Type | Purpose | Guardrail |
|---|---|---|---|
| `uTime` | float | phase animation | freeze toggle for debugging |
| `uResolution` | vec2 | pixel normalization | update on resize |
| `uNoiseScale` | float | turbulence detail | clamp 0.5-8.0 |
| `uExposure` | float | tone control | clamp 0.8-1.4 |

### Precision + Derivative Notes
- Use `highp` in fragment shader for mobile stability when gradients are subtle.
- Use `fwidth`-based smoothing for contour edges.

### Before / After Anti-Aliasing Snippet

```glsl
// Before
float ring = step(0.5, fract(d * 8.0));

// After
float w = fwidth(d * 8.0);
float ring = smoothstep(0.5 - w, 0.5 + w, fract(d * 8.0));
```

### Mobile GPU Release Criteria
- No temporal shimmer on iOS Safari and Adreno Chrome.
- Shader compile time < 40ms cold start.
- Visual delta against desktop reference <= agreed art threshold.

