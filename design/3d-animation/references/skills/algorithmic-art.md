---
name: "algorithmic-art"
title: "Algorithmic Art"
description: "Use for creating generative art using p5.js with seeded randomness, algorithmic philosophies, and interactive parameter controls."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/algorithmic-art.md`
- Examples: `examples/skills/algorithmic-art.md`
- Templates: `algorithmic-art__templates/viewer.html`, `algorithmic-art__templates/generator_template.js`
- License: `algorithmic-art__LICENSE.txt`

## Linked Package Files

- Adjacent: `references/skills/glsl-shader-alchemist.md` — for shader-based visual effects
- Adjacent: `references/skills/threejs-postprocessing.md` — for post-processing on 3D canvases
- Validation: `references/skills/threejs-fundamentals.md` — for canvas and rendering basics

## Purpose

Algorithmic philosophies are computational aesthetic movements expressed through code. This skill guides the creation of generative art using p5.js, from defining an algorithmic philosophy to producing a self-contained interactive HTML artifact.

## When to Use

- When creating generative or procedural art
- When building p5.js-based interactive visual compositions
- When designing algorithmic visual systems with seeded randomness
- When producing Art Blocks-style parametric art pieces

## Workflow

1. Create an algorithmic philosophy as a markdown document explaining the generative aesthetic, its principles, and visual language.
2. Read `algorithmic-art__templates/viewer.html` using the Read tool.
3. Study the exact structure, styling, and branding of the template.
4. Use the template as the literal starting point — not just inspiration.
5. Keep all fixed sections exactly as shown in the template (header, sidebar structure, colors/fonts, seed controls, action buttons).
6. Replace only the variable sections marked in the template comments (algorithm, parameters, UI controls for parameters).
7. Output both the philosophy document and the single HTML artifact.

## Quality Standards

- Always use seeded randomness for reproducibility (Art Blocks pattern).
- Parameters must emerge naturally from the algorithmic philosophy.
- The HTML artifact must be self-contained and work immediately in any browser.
- Use p5.js from CDN, not local files.
- All parameter controls must update the visualization in real time.

## Technical Rules

- Always use `randomSeed(seed)` and `noiseSeed(seed)` for reproducibility.
- Parameters should control meaningful qualities: quantities, scales, probabilities, ratios, angles, thresholds.
- Start the HTML from the provided `viewer.html` template, not from scratch.
- The artifact must include p5.js from CDN, the algorithm, parameter controls, and UI in a single file.

## Validation

Output must include:
1. An algorithmic philosophy document (markdown or text) explaining the generative aesthetic.
2. A single HTML artifact — self-contained interactive generative art built from the `viewer.html` template.

The HTML artifact must work immediately in claude.ai artifacts or any browser.

## Restrictions

- Do not skip visual inspection of the final output.
- Do not deliver unvalidated or untested assets.
- Do not hardcode values that should be controlled by parameters.
- Do not create the HTML from scratch — always start from the template.

## Output Requirements

- Algorithmic philosophy as markdown or inline text.
- Single HTML artifact built from `algorithmic-art__templates/viewer.html`.
- The artifact must be self-contained with no external dependencies other than p5.js CDN.

## Stage 3.7 Extension: Production Diagnostics and Release Gates

### Failure Modes to Catch Before Release
- Seed replay mismatch: same `seed` produces different pixel output across refreshes.
- Parameter overflow: UI allows values outside approved artistic range and breaks composition density.
- Export drift: runtime preview canvas differs from export canvas ratio, cropping key motifs.
- Interactive lag: parameter scrubbing causes frame stalls on mid-tier devices.
- Fallback gap: static poster mode missing when interaction budget is exceeded.

### Diagnostics Workflow (Algorithmic Art)
1. Lock a test seed set (`seed-a`, `seed-b`, `seed-c`) and replay each seed three times per browser.
2. Validate parameter clamps by forcing min/max values and confirming safe output boundaries.
3. Compare preview vs export dimensions (`1x`, `2x`, print size) for framing consistency.
4. Run interaction stress pass (rapid slider changes for 30s) and record frame stability.
5. Trigger reduced-motion mode and verify static poster fallback with preserved composition.

### Release Evidence Package
- Seed used for approval (single canonical integer).
- Parameter JSON snapshot (all tunables + clamp ranges).
- Canvas dimensions for preview and export.
- Browser replay notes (Chrome/Safari/Firefox consistency summary).
- Export hash or side-by-side visual comparison note documenting replay fidelity.

### Acceptance Gates
- Same seed + parameter JSON reproduces matching composition structure in all target browsers.
- No parameter setting produces empty, clipped, or NaN-driven output.
- Export framing matches approved preview framing within documented tolerance.
- Interactive mode stays within budget, or static fallback is automatically selected.

### Validation Neighbors
- `glsl-shader-alchemist` for procedural math and visual-function sanity checks.
- `threejs-postprocessing` for color/contrast finishing when canvas output is composited.
- `threejs-fundamentals` for canvas lifecycle and performance baselines.

