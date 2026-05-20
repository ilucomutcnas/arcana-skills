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

