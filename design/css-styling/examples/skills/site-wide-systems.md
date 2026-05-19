# Examples — Site-Wide Systems

## Example: page shell rules

```css
.page-shell {
  min-height: 100dvh;
  background: var(--color-bg);
  color: var(--color-fg);
}

.page-section {
  padding-block: clamp(3rem, 6vw, 6rem);
}

.content-measure {
  width: min(100%, 68ch);
}
```

## Example: semantic text roles

```css
.text-display { font-size: clamp(2.25rem, 5vw, 4.5rem); line-height: 0.98; }
.text-heading { font-size: clamp(1.5rem, 2.8vw, 2.5rem); line-height: 1.08; }
.text-body { font-size: 1rem; line-height: 1.6; }
.text-meta { font-size: 0.875rem; line-height: 1.4; color: var(--color-muted); }
```

## Stage 3.5 Extension: Multi-Page Consistency Remediation

### Drift Table

| Page Family | Drift Found | Remediation |
|---|---|---|
| Marketing | duplicated button tokens | remap to shared `--action-*` tokens |
| Docs | custom heading sizes | align to semantic text roles |
| App shell | ad-hoc spacing utilities | migrate to layout primitives |
| Account pages | deep selector overrides | component-scoped classes + token usage |

### Rollout Phases
1. **Pilot**: migrate account + one marketing page family.
2. **Page family migration**: docs/app shell in parallel with QA matrix.
3. **Regression snapshot**: visual compare on 5 key templates.
4. **Cleanup**: delete deprecated overrides and dead selectors.

### Acceptance Criteria
- No new deep descendant selectors in shared styles.
- Every override includes owner and expiry milestone.
- Brand refresh remains possible by changing tokens/components only.
