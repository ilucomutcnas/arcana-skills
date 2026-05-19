# Fixing Motion Performance — Examples

## Animate Transform Instead of Layout Properties

```css
/* before — triggers layout */
.panel { transition: width 0.3s; }

/* after — GPU-composited */
.panel { transition: transform 0.3s; }
```

## Scroll-Linked: Use CSS Instead of JS

```css
/* before */
/* window.addEventListener('scroll', () => el.style.opacity = scrollY / 500) */

/* after — CSS native */
.reveal {
  animation: fade-in linear;
  animation-timeline: view();
}
```

## Batch Reads Before Writes (FLIP Pattern)

```js
// before — layout thrash
el.style.left = el.getBoundingClientRect().left + 10 + 'px';

// after — measure once, animate via transform
const first = el.getBoundingClientRect();
el.classList.add('moved');
const last = el.getBoundingClientRect();
el.style.transform = `translateX(${first.left - last.left}px)`;
requestAnimationFrame(() => {
  el.style.transition = 'transform 0.3s';
  el.style.transform = '';
});
```

## Respect Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
```

## Audit Command Usage

```
/fixing-motion-performance
  Apply motion performance constraints to any UI animation work.

/fixing-motion-performance <file>
  Review the file and report:
  - violations (quote the exact line or snippet)
  - why it matters (one short sentence)
  - a concrete fix (code-level suggestion)
```

## Stage 3 Drawer + Accordion Motion Remediation

## Stage 3 Concrete Drawer + Accordion Motion Remediation
### Before
```css
.drawer { left: -320px; transition: left 240ms ease; }
.drawer.open { left: 0; }
.accordion-panel { max-height: 0; transition: max-height 300ms ease; }
.accordion-panel.open { max-height: 1000px; }
```

### After
```css
.drawer { transform: translateX(-100%); opacity: 0; transition: transform 180ms ease, opacity 180ms ease; }
.drawer.open { transform: translateX(0); opacity: 1; }
.accordion-panel { transform-origin: top; transform: scaleY(0.98); opacity: 0; transition: transform 140ms ease, opacity 140ms ease; }
.accordion-panel.open { transform: scaleY(1); opacity: 1; }
@media (prefers-reduced-motion: reduce) {
  .drawer, .accordion-panel { transition: none; }
}
```

### Stability checks
- Opening drawer preserves scroll position.
- Focus remains on toggled control until panel is interactable, then moves to first heading.
- Rapid open/close (10 times in 5 seconds) shows no dropped focus and no stuck states.
