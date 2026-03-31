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
