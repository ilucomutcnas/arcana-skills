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
