# Scroll Experience — Examples

## Library Comparison

| Library | Best For | Learning Curve |
|---------|----------|----------------|
| GSAP ScrollTrigger | Complex animations | Medium |
| Framer Motion | React projects | Low |
| Locomotive Scroll | Smooth scroll + parallax | Medium |
| Lenis | Smooth scroll only | Low |
| CSS scroll-timeline | Simple, native | Low |

## GSAP ScrollTrigger Setup

```javascript
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

gsap.to(".element", {
  scrollTrigger: {
    trigger: ".element",
    start: "top center",
    end: "bottom center",
    scrub: true,
    markers: true, // Remove in production
  },
  x: 200,
  opacity: 1,
  duration: 1,
});
```

## Framer Motion Scroll (React)

```jsx
import { motion, useScroll, useTransform } from "framer-motion";

function ScrollComponent() {
  const { scrollYProgress } = useScroll();
  const opacity = useTransform(scrollYProgress, [0, 0.5], [0, 1]);
  const scale = useTransform(scrollYProgress, [0, 1], [0.8, 1]);

  return (
    <motion.div style={{ opacity, scale }}>
      Content
    </motion.div>
  );
}
```

## CSS Native Scroll Animation (2024+)

```css
@keyframes fade-in {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.element {
  animation: fade-in linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}
```

## Scroll-Driven Product Story Release Example

### Section Timing Table

| Section | Scroll Span | Effect | Pinning |
|---|---:|---|---|
| Hero intro | 0-18vh | headline parallax + model fade-in | pinned |
| Feature reveal | 18-72vh | camera dolly + text stepper | pinned |
| Spec breakdown | 72-130vh | chart scrub + counters | unpinned |
| CTA | 130-160vh | subtle fade + scale | unpinned |

### Library / Tech Choice Notes
- GSAP ScrollTrigger for deterministic scrub + pin control.
- Native IntersectionObserver for analytics beacons.
- CSS `scroll-timeline` reserved for non-critical enhancement only.

### Reduced-Motion Fallback
- Replace scrubbed transforms with discrete fade-in sections.
- Disable pinning and preserve natural document flow.

### Cleanup / Unmount Checklist
- [ ] Kill ScrollTrigger instances on route change.
- [ ] Remove resize/scroll listeners.
- [ ] Reset inline transforms before unmount.

### CLS / Layout Stability QA Matrix

| Check | Target | Result Gate |
|---|---|---|
| CLS | < 0.1 | Block release if exceeded |
| Hero height shift | 0px after hydration | Block release |
| Mobile viewport resize jump | none | Must pass Safari iOS |

