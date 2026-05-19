# Frontend Alchemy — Examples

## Design Feasibility and Impact Index (DFII)

```
DFII = (Impact + Fit + Feasibility + Performance) − Consistency Risk
```

Rate each dimension 1-5:

| Dimension | Question |
|-----------|----------|
| Impact | Does this make the interface notably better? |
| Fit | Does it belong in this design language? |
| Feasibility | Can it be built cleanly? |
| Performance | Does it run well? |
| Consistency Risk | Does it create drift from the system? |

**Range:** -5 → +15. Proceed if ≥ 6.

## Pre-Implementation Questions

1. Who is this for, emotionally?
2. Should this feel trustworthy, exciting, calm, or provocative?
3. Is memorability or clarity more important?
4. Will this scale to other pages/components?

## Core Principles

- Clarity beats cleverness
- Restraint beats excess
- Precision beats decoration
- Intentionality beats defaults

## Stage 3.5 Extension: Premium Analytics Dashboard Scenario

### Visual Concept Table

| Dimension | Decision |
|---|---|
| atmosphere | calm precision with high-contrast numerics |
| layout rhythm | alternating dense metric rows and breathing summary bands |
| interaction polish | subtle card lift + focused chart crosshair |
| restraint risk | overusing glow effects on all KPI cards |
| implementation constraint | tokenized shadows/colors, no bespoke one-off palette |

### DFII Scoring Example

`DFII = (Impact 4 + Fit 3 + Feasibility 3 + Performance 2) - (Consistency Risk 2) = 10`

Result: proceed, but cap decorative effects to hero KPI row only.

### Acceptance Criteria
- High-craft styling without ornamental overload on secondary surfaces.
- Accessibility floors met (contrast, focus visibility, reduced motion).
- Performance budget preserved for dashboard route CSS and animation cost.
- Handoff includes maintainable token/layer implementation notes.
