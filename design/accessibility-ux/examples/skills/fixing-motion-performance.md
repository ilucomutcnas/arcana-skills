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
