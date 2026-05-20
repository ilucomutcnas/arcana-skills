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

