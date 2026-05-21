# Makepad Shader Lab — Examples

## Solid Color Shader

```rust
<View> {
    show_bg: true
    draw_bg: {
        color: #FF0000

        fn pixel(self) -> vec4 {
            return self.color;
        }
    }
}
```

## Rounded Box with Border

```rust
<View> {
    show_bg: true
    draw_bg: {
        color: #333333
        border_color: #666666
        border_radius: 8.0
        border_size: 1.0

        fn pixel(self) -> vec4 {
            let sdf = Sdf2d::viewport(self.pos * self.rect_size);
            sdf.box(1.0, 1.0,
                    self.rect_size.x - 2.0,
                    self.rect_size.y - 2.0,
                    self.border_radius);
            sdf.fill_keep(self.color);
            sdf.stroke(self.border_color, self.border_size);
            return sdf.result;
        }
    }
}
```

## Horizontal Gradient

```rust
<View> {
    show_bg: true
    draw_bg: {
        color: #FF0000
        color_2: #0000FF

        fn pixel(self) -> vec4 {
            let t = self.pos.x;  // Horizontal gradient
            return mix(self.color, self.color_2, t);
        }
    }
}
```

## Key Rules

1. Always use `show_bg: true` to enable background shader.
2. Use `Sdf2d::viewport()` to create SDF context.
3. Return `vec4` (RGBA) from `fn pixel()`.
4. Uniforms must be declared before shader functions.
5. Use `self.` prefix to access uniforms and built-ins.

## Makepad Shader Bug Triage Example

### Symptom Table

| Symptom | Likely Cause | Severity |
|---|---|---|
| Rounded box corners flicker | Sdf2d distance precision + animated radius race | Blocking |
| Gradient banding in dark theme | low precision + no dither | Major |
| Edge halo after hover | blend order mismatch | Major |

### Before / After Shader Snippet

```rust
// Before
let edge = smoothstep(radius - 0.01, radius + 0.01, dist);
let col = mix(color_a, color_b, uv.y);

// After
let aa = max(fwidth(dist), 0.0015);
let edge = smoothstep(radius - aa, radius + aa, dist);
let col = dither_gradient(mix(color_a, color_b, uv.y), self.time);
```

### Uniform Update Checklist
- [ ] Hover/pressed uniforms update in same frame as state transition.
- [ ] Radius uniform clamped to component bounds.
- [ ] Time uniform monotonic and reset-safe on re-mount.
- [ ] Theme colors converted once and cached.

### Artifact Acceptance Criteria
- No visible corner jitter during 5s hover loop.
- No gradient bands at 50% brightness on OLED mobile test.
- Fallback solid fill path available when custom shader compilation fails.

