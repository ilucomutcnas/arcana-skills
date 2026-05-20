# Makepad Animator — Examples

## Basic Hover Animation

```rust
<Button> {
    text: "Hover Me"

    animator: {
        hover = {
            default: off

            off = {
                from: { all: Forward { duration: 0.15 } }
                apply: {
                    draw_bg: { color: #333333 }
                }
            }

            on = {
                from: { all: Forward { duration: 0.15 } }
                apply: {
                    draw_bg: { color: #555555 }
                }
            }
        }
    }
}
```

## Combined Hover and Pressed States

```rust
<View> {
    animator: {
        hover = {
            default: off
            off = {
                from: { all: Forward { duration: 0.2 } }
                apply: { draw_bg: { color: #222222 } }
            }
            on = {
                from: { all: Forward { duration: 0.2 } }
                apply: { draw_bg: { color: #444444 } }
            }
        }

        pressed = {
            default: off
            off = {
                from: { all: Forward { duration: 0.1 } }
                apply: { draw_bg: { scale: 1.0 } }
            }
            on = {
                from: { all: Forward { duration: 0.1 } }
                apply: { draw_bg: { scale: 0.95 } }
            }
        }
    }
}
```

## Focus State with Border Animation

```rust
<TextInput> {
    animator: {
        focus = {
            default: off

            off = {
                from: { all: Forward { duration: 0.2 } }
                apply: {
                    draw_bg: {
                        border_color: #444444
                        border_size: 1.0
                    }
                }
            }

            on = {
                from: { all: Forward { duration: 0.2 } }
                apply: {
                    draw_bg: {
                        border_color: #0066CC
                        border_size: 2.0
                    }
                }
            }
        }
    }
}
```

## Key Rules

1. Always set `default:` for initial state.
2. Use `Forward` for smooth transitions (0.1–0.3s).
3. Use `Snap` for instant state changes (disabled states).
4. Animate shader uniforms in `draw_bg`, `draw_text`, etc.

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

