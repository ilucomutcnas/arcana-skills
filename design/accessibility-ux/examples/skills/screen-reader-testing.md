# Screen Reader Testing — Examples

## Testing Priority Matrix

| Screen Reader | Platform  | Browser        | Usage |
|---------------|-----------|----------------|-------|
| NVDA          | Windows   | Firefox/Chrome | ~31%  |
| JAWS          | Windows   | Chrome/IE      | ~40%  |
| VoiceOver     | macOS/iOS | Safari         | ~15%  |
| TalkBack      | Android   | Chrome         | ~10%  |
| Narrator      | Windows   | Edge           | ~4%   |

## Minimum Coverage

1. NVDA + Firefox (Windows)
2. VoiceOver + Safari (macOS)
3. VoiceOver + Safari (iOS)

## VoiceOver Quick Reference

```
VO = Ctrl + Option (VoiceOver modifier)
VO + Right/Left   Navigate elements
VO + Space         Activate element
VO + U             Open rotor
VO + Cmd + H       Next heading
Tab                Next focusable element
```

## NVDA Quick Reference

```
Insert = NVDA modifier
H                  Next heading
F                  Next form field
D                  Next landmark
NVDA + F7          Elements list
NVDA + Space       Toggle browse/focus mode
```

## Accessible Modal Pattern

```html
<div role="dialog" aria-modal="true"
     aria-labelledby="dialog-title"
     aria-describedby="dialog-desc">
  <h2 id="dialog-title">Confirm Delete</h2>
  <p id="dialog-desc">This action cannot be undone.</p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

## Live Region Patterns

```html
<!-- Status (polite) -->
<div role="status" aria-live="polite" aria-atomic="true">
  3 items added to cart
</div>

<!-- Alert (assertive) -->
<div role="alert" aria-live="assertive">
  Error: Form submission failed
</div>
```

For detailed checklists, test scripts, and more code patterns, see `screen-reader-testing__resources/implementation-playbook.md`.
