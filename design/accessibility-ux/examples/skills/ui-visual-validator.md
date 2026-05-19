# UI Visual Validator — Examples

## Assessment Framework

Start every evaluation with: "From the visual evidence, I observe..."

## Evaluation Categories

### Layout and Spacing
- Measure padding, margin, and gap values precisely.
- Compare against design tokens or specification.
- Check alignment across grid lines.

### Typography
- Verify font family, size, weight, line-height.
- Check for text truncation or overflow.
- Confirm heading hierarchy visually matches semantic structure.

### Color and Contrast
- Measure text-to-background contrast ratio (target: 4.5:1 for text, 3:1 for UI).
- Verify focus indicator contrast.
- Check dark mode and high-contrast mode rendering.

### Responsive Behavior
- Test at standard breakpoints: 320px, 768px, 1024px, 1440px.
- Verify content reflows correctly at 200% zoom.
- Check that no horizontal scrolling appears at 320px width.

## Validation Checklist

```markdown
## Visual Validation Checklist

### Goal Achievement
- [ ] Modification goal clearly achieved (visual evidence)
- [ ] No regression from previous state
- [ ] Design specification matched

### Accessibility Visual Checks
- [ ] Focus indicators visible on all interactive elements
- [ ] Color contrast meets WCAG AA
- [ ] Content reflows at 200% zoom
- [ ] No information conveyed by color alone

### Edge Cases
- [ ] Long text content handled (truncation, wrapping)
- [ ] Empty states rendered correctly
- [ ] Loading states visible and accessible
- [ ] Error states visually distinct and accessible
```

## Output Template

```
From the visual evidence, I observe:
- [Observation 1 with measurement]
- [Observation 2 with measurement]

Goal status: [Achieved / Partially achieved / Not achieved]

Issues found:
1. [Issue with specific remediation]

Accessibility assessment:
- [Contrast / focus / reflow findings]
```

## Stage 3 Accessibility Visual Report

## Stage 3 Accessibility Visual Validation Report
| Check | Evidence | Result | Remediation |
|---|---|---|---|
| Focus outline visibility | 2px ring visible on button/input links at 100/200% zoom | Pass | None |
| Contrast | Body text 7.1:1, helper text 4.7:1, error text 5.2:1 | Pass | None |
| Touch targets | Icon buttons min 44x44 px except close icon 36x36 | Fail | Increase close icon hit-area via padding wrapper |
| Zoom/text spacing | Layout intact at 400% and custom letter/line spacing | Pass | None |
| Forced colors | Active card border lost in forced-colors mode | Fail | Add system color border token |
| Dark mode | Error hint too dim in dark mode | Fail | Raise token contrast to >=4.5:1 |
