# Routing Guide

## Rules

- Choose the narrowest matching skill first.
- Open `references/skills/<slug>.md` for full doctrine and commands.
- Open `examples/skills/<slug>.md` for task routing patterns.
- Always check `shared-rules/ANTI-PATTERNS.md` for what not to do.

## Quick Navigation

### Core Engine
- **library-architecture** -> `references/skills/library-architecture.md`

### Quality Verification
- **browser-accuracy** -> `references/skills/browser-accuracy.md`
- **benchmarks-profiling** -> `references/skills/benchmarks-profiling.md`
- **corpus-diagnostics** -> `references/skills/corpus-diagnostics.md`

### Contributor Operations
- **development-workflow** -> `references/skills/development-workflow.md`
- **packaging-release** -> `references/skills/packaging-release.md`
- **demo-dogfooding** -> `references/skills/demo-dogfooding.md`

### Strategy and History
- **priorities-roadmap** -> `references/skills/priorities-roadmap.md`
- **research-log** -> `references/skills/research-log.md`
- **architecture-review** -> `references/skills/architecture-review.md`

## Routing by Task Type

- **Core engine change** -> library-architecture + browser-accuracy + corpus-diagnostics + research-log
- **Browser sweep** -> browser-accuracy + corpus-diagnostics + benchmarks-profiling
- **Performance work** -> benchmarks-profiling + library-architecture
- **Corpus expansion** -> corpus-diagnostics + browser-accuracy + priorities-roadmap
- **Release prep** -> packaging-release + benchmarks-profiling + browser-accuracy + development-workflow
- **New demo** -> demo-dogfooding + library-architecture + development-workflow
- **Onboarding** -> development-workflow + priorities-roadmap + architecture-review
- **Diff review** -> architecture-review + library-architecture + research-log

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md)
- [`manifest.json`](manifest.json)
