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

## Makepad Button/Card Transition Release Example

### State Transition Table

| State | Entry Trigger | Exit Trigger | Motion Token | Release Expectation |
|---|---|---|---|---|
| `default` | initial/load | hover/focus/disabled | none | Stable baseline colors |
| `hover` | pointer enter | pointer leave/press | `fast-120ms` | Elevation + subtle scale |
| `pressed` | pointer down/keyboard activate | pointer up | `snap-0ms` for scale, `80ms` color | Immediate tactile response |
| `disabled` | form lock / async pending | enabled | `snap-0ms` | No hover/press animation |
| `focus` | keyboard tab | blur | `standard-160ms` ring | WCAG-visible focus ring |

### Snap vs Forward Timing Decisions
- Use snap for interaction-critical transforms (`pressed` scale).
- Use forward easing for decorative transitions (`hover` glow).
- Reject builds where disabled state still animates.

### Reduced-Motion Mapping
- Map `hover` scale animation to color-only change when reduced motion active.
- Collapse card entrance motion to opacity fade <= 80ms.

### Failure-State Checklist
- [ ] Focus ring visible without pointer.
- [ ] Rapid hover/press spam does not deadlock state machine.
- [ ] Disabled state ignores all pointer/key events.
- [ ] Motion tokens resolve from shared design token source, not literals.

