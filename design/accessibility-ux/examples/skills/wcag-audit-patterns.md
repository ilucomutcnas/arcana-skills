# WCAG Audit Patterns — Examples

## Automated Testing with axe-core

```javascript
const axe = require('axe-core');

async function runAccessibilityAudit(page) {
  await page.addScriptTag({ path: require.resolve('axe-core') });

  const results = await page.evaluate(async () => {
    return await axe.run(document, {
      runOnly: {
        type: 'tag',
        values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']
      }
    });
  });

  return {
    violations: results.violations,
    passes: results.passes,
    incomplete: results.incomplete
  };
}
```

## Playwright Accessibility Test

```javascript
test('should have no accessibility violations', async ({ page }) => {
  await page.goto('/');
  const results = await runAccessibilityAudit(page);
  expect(results.violations).toHaveLength(0);
});
```

## CLI Tools

```bash
npx @axe-core/cli https://example.com
npx pa11y https://example.com
lighthouse https://example.com --only-categories=accessibility
```

## Fix: Missing Form Labels

```html
<!-- Before -->
<input type="email" placeholder="Email" />

<!-- After: Option 1 — Visible label -->
<label for="email">Email address</label>
<input id="email" type="email" />

<!-- After: Option 2 — aria-label -->
<input type="email" aria-label="Email address" />
```

## Fix: Insufficient Color Contrast

```css
/* Before: 2.5:1 contrast */
.text { color: #767676; }

/* After: 4.5:1 contrast */
.text { color: #595959; }
```

## Fix: Keyboard-Accessible Custom Widget

```javascript
class AccessibleDropdown extends HTMLElement {
  connectedCallback() {
    this.setAttribute('tabindex', '0');
    this.setAttribute('role', 'combobox');
    this.setAttribute('aria-expanded', 'false');

    this.addEventListener('keydown', (e) => {
      switch (e.key) {
        case 'Enter':
        case ' ':
          this.toggle();
          e.preventDefault();
          break;
        case 'Escape':
          this.close();
          break;
        case 'ArrowDown':
          this.focusNext();
          e.preventDefault();
          break;
        case 'ArrowUp':
          this.focusPrevious();
          e.preventDefault();
          break;
      }
    });
  }
}
```

## Focus Visible Indicator

```css
:focus {
  outline: 3px solid #005fcc;
  outline-offset: 2px;
}
```

For detailed WCAG checklists and remediation patterns, see `wcag-audit-patterns__resources/implementation-playbook.md`.

## Stage 3 Multi-Page Audit Plan

## Stage 3 Multi-Page WCAG Audit Plan
### Sample strategy
| Template | Count | Sampled pages | Reason |
|---|---:|---:|---|
| Product detail | 84 | 8 | Highest traffic + purchase dependency |
| Checkout steps | 6 | 6 | Critical conversion flow |
| Account settings | 12 | 4 | Authenticated complexity |

### Criteria mapping by flow
- Product detail: 1.1.1, 1.3.1, 1.4.3, 2.4.6
- Checkout modal: 2.1.1, 2.4.3, 3.3.1, 4.1.3
- Account settings: 1.3.5, 2.4.7, 3.3.2

### Automated vs manual split
- Automated: axe-core + Lighthouse across all sampled pages.
- Manual: keyboard traversal, SR narration checks, forced-colors and zoom at 200/400%.

### Severity-ranked backlog seed
1. Critical: modal focus-loss blocks payment submission.
2. High: status message not announced after coupon apply.
3. Medium: insufficient dark-mode helper-text contrast.

### Retest release criteria
Release only when critical/high issues are closed with evidence, medium issues have owner+date, and regression checks pass on two supported browser/AT pairs.
