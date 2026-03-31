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
