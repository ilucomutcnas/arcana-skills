# Development Workflow — Examples

## Example: Repo Analysis Task Routing

**Task:** "I need to understand how this repo is maintained and what is safe to change."

**Route:**
1. development-workflow — command surface
2. architecture-review — system-level guardrails
3. priorities-roadmap — active priorities
4. original-docs/AGENTS.md — preserved contributor notes

## Core Commands Quick Reference

```sh
bun install          # Setup
bun start            # Stable demo pages
bun run check        # Typecheck and lint
bun test             # Invariant suite
bun run build:package  # Emit dist/
bun run package-smoke-test  # Tarball verification
```
