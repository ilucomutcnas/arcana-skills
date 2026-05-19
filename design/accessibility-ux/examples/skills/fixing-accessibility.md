# Fixing Accessibility — Examples

## Icon-Only Button: Add aria-label

```html
<!-- before -->
<button><svg>...</svg></button>

<!-- after -->
<button aria-label="Close"><svg aria-hidden="true">...</svg></button>
```

## Div as Button: Use Native Element

```html
<!-- before -->
<div onclick="save()">Save</div>

<!-- after -->
<button onclick="save()">Save</button>
```

## Form Error: Link with aria-describedby

```html
<!-- before -->
<input id="email" />
<span>Invalid email</span>

<!-- after -->
<input id="email" aria-describedby="email-err" aria-invalid="true" />
<span id="email-err">Invalid email</span>
```

## Dynamic Content: Use aria-live

```html
<!-- before -->
<div id="results">New results loaded</div>

<!-- after -->
<div id="results" role="status" aria-live="polite">New results loaded</div>
```

## Audit Command Usage

```
/fixing-accessibility
  Apply accessibility constraints to any UI work in this conversation.

/fixing-accessibility <file>
  Review the file and report:
  - violations (quote the exact line or snippet)
  - why it matters (one short sentence)
  - a concrete fix (code-level suggestion)
```

## Stage 3 Form + Modal Remediation Snapshot

## Stage 3 Concrete Form + Modal Remediation
### Before (problematic)
```jsx
<dialog open>
  <form onSubmit={submit}>
    <input id="email" />
    <p id="emailError">Invalid email</p>
    <button>Save</button>
  </form>
</dialog>
```

### After (fixed)
```jsx
<dialog open aria-labelledby="profileTitle" aria-describedby="formSummary" onKeyDown={onDialogKeyDown}>
  <h2 id="profileTitle">Update profile</h2>
  <div id="formSummary" tabIndex={-1} role="alert">Please correct 1 field below.</div>
  <form onSubmit={submit}>
    <label htmlFor="email">Email address</label>
    <input id="email" aria-invalid={hasEmailError} aria-describedby={hasEmailError ? "emailError" : undefined} />
    {hasEmailError && <p id="emailError">Enter a valid email like name@example.com</p>}
    <button type="submit">Save</button>
    <button type="button" onClick={closeModal}>Cancel</button>
  </form>
</dialog>
```

### Keyboard path evidence
| Action | Expected result |
|---|---|
| Tab | Moves summary → first invalid field → Save → Cancel |
| Shift+Tab | Reverses order without escaping modal trap |
| Escape | Closes modal and restores focus to invoking button |

### Acceptance checks
- Error summary receives focus after invalid submit.
- `aria-describedby` points to active error text only when error exists.
- Escape closes modal and returns focus to opener.
- No keyboard trap; focus cycle stays inside modal when open.
