# Web Design Codex — Examples

## Guidelines Source

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

## Workflow

1. Fetch guidelines from the source URL above using WebFetch.
2. Read the specified files or ask the user which files to review.
3. Apply all rules from the fetched guidelines.
4. Output findings in terse `file:line` format.

## Output Format

Findings follow the format defined in the fetched guidelines, typically:

```
src/components/Button.tsx:42 — Missing focus-visible outline
src/components/Modal.tsx:18 — Dialog missing aria-labelledby
src/pages/index.tsx:7 — Page title not descriptive
```

## Key Principle

Always fetch fresh guidelines before each review. The fetched content is the authoritative source for all rules and output format instructions.
