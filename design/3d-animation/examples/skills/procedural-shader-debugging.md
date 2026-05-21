# Procedural Shader Debugging — Example

## Scenario
A product hero uses a procedural iridescent ShaderMaterial plus bloom pass. On Safari iOS, highlights flicker and shadows posterize during scroll-driven camera motion.

## Symptom Table

| Symptom | Frequency | Impact | Blocking |
|---|---:|---|---|
| Flickering specular bands | 100% on iOS Safari | Distracting hero artifact | Yes |
| Bloom halo clipping | Intermittent desktop | Brand quality issue | Yes |
| Gradient banding in dark ramps | Mobile + low brightness | Perceptual quality loss | Yes |

## Suspected Cause Matrix

| Suspect | Signal | Test |
|---|---|---|
| `mediump` precision in fragment stage | iOS-only instability | Force `highp` and compare |
| Time uniform drift | artifact increases over long sessions | freeze time at constant |
| Pass order error | bloom clips post-tonemap | reorder composer passes |
| Color-space mismatch | over-saturated bloom | align output colorSpace and toneMapping |

## Diagnostic Steps

1. Reduce scene to one mesh, single light, no scroll transforms.
2. Enable debug color outputs: UV map, normal map, luminance-only.
3. Freeze `uTime` and validate flicker persistence.
4. Force DPR=1 and fixed render target size.
5. Reorder passes: RenderPass -> custom shader -> bloom -> output.
6. Run browser/GPU matrix and capture metrics.

## Before/After Snippet

```glsl
// Before
precision mediump float;
vec3 n = normalize(vNormal);
float rim = pow(1.0 - dot(n, vViewDir), 8.0);

// After
precision highp float;
vec3 n = normalize(max(length(vNormal), 1e-5) * normalize(vNormal));
float ndv = clamp(dot(normalize(n), normalize(vViewDir)), 0.0, 1.0);
float rim = pow(max(1.0 - ndv, 0.0), 6.0);
```

## Cross-Browser/GPU Evidence

| Platform | Result | Notes |
|---|---|---|
| Chrome 136 / RTX 3060 | Pass | Stable at DPR 1.5 |
| Firefox 128 / RX 6800 | Pass | Slight noise within threshold |
| Safari 18 / M2 | Pass | No flicker after highp + pass reorder |
| iOS Safari 18 / A16 | Pass (fallback bloom) | Bloom quality reduced, stable |

## Acceptance Criteria

- No NaN flashes or temporal flicker in 60s idle run.
- Color-space consistent between base pass and bloom output.
- Mobile fallback path documented and enabled.
- Performance remains within agreed frame budget.

## Handoff Notes

- Creative: verify visual intent against approved stills.
- Front-end: keep debug toggles behind non-production flag.
- QA: rerun matrix when tone mapping, DPR cap, or pass ordering changes.
