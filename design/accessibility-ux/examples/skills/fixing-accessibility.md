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
