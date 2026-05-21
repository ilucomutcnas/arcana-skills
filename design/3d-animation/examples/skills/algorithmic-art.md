# Algorithmic Art — Examples

## Seeded Randomness (Art Blocks Pattern)

```javascript
// ALWAYS use a seed for reproducibility
let seed = 12345; // or hash from user input
randomSeed(seed);
noiseSeed(seed);
```

## Parameter Structure

```javascript
let params = {
  seed: 12345,  // Always include seed for reproducibility
  // colors
  // Add parameters that control YOUR algorithm:
  // - Quantities (how many?)
  // - Scales (how big? how fast?)
  // - Probabilities (how likely?)
  // - Ratios (what proportions?)
  // - Angles (what direction?)
  // - Thresholds (when does behavior change?)
};
```

## Basic p5.js Setup

```javascript
function setup() {
  createCanvas(1200, 1200);
  // Initialize your system
}

function draw() {
  // Your generative algorithm
  // Can be static (noLoop) or animated
}
```

## Output Workflow

1. Create the algorithmic philosophy as markdown explaining the generative aesthetic.
2. Read `algorithmic-art__templates/viewer.html` as the literal starting point.
3. Keep all FIXED sections (header, sidebar structure, colors/fonts, seed controls, action buttons).
4. Replace only the VARIABLE sections marked in comments (algorithm, parameters, UI controls).
5. Deliver both the philosophy document and the single HTML artifact.

## Seeded Generative Poster Release Example

### Seed + Parameter Table

| Parameter | Value | Range | Release Rule |
|---|---:|---:|---|
| `seed` | `842137` | integer | Must replay identical pixels for same seed |
| `gridDensity` | `72` | 24-120 | Reject if causes frame budget overrun |
| `noiseScale` | `0.006` | 0.001-0.02 | Clamp to avoid alias shimmer |
| `paletteMode` | `duotone-ink` | enum | Must map to approved brand palette |
| `strokeAlpha` | `0.82` | 0.2-1.0 | Keep readability contrast for overlays |

### Deterministic Replay Rule
- Always call `randomSeed(seed)` and `noiseSeed(seed)` before generating strokes.
- Export metadata sidecar (`seed`, parameter JSON, canvas size) with each approved poster.
- QA reruns seed on Chrome + Safari and compares histogram drift within 1%.

### Canvas Sizing and Export Rules
- Author at `2400x3000` for print master; runtime preview at `1200x1500`.
- Use devicePixelRatio cap of `2` for interactive preview.
- Export PNG and SVG-safe annotation overlay (no binary assets committed to repo).

### Performance Acceptance Checks
- Desktop render <= 120ms first frame for static poster mode.
- Interactive mode sustained >= 45 FPS on mid-range laptop.
- Memory budget <= 180MB total tab usage while parameter scrubbing.

### Fallback / Static Poster Note
- If motion mode exceeds budget or prefers-reduced-motion is enabled, switch to static seeded render and disable animated perturbation loop.

