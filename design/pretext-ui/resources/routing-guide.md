# Routing Guide

## Rules

- Choose the narrowest matching skill first.
- Open `references/skills/{slug}.md` for full doctrine and commands.
- Open `examples/skills/{slug}.md` for task routing patterns.
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

## Extended Routing Scenarios

- **Public API changes** -> library-architecture + corpus-diagnostics + architecture-review
- **Layout mismatch in page/demo** -> browser-accuracy + library-architecture + corpus-diagnostics
- **Browser sweep (release gate)** -> browser-accuracy + development-workflow + corpus-diagnostics
- **Performance regression** -> benchmarks-profiling + library-architecture + architecture-review
- **Corpus/canary update** -> corpus-diagnostics + browser-accuracy + research-log
- **Release candidate** -> packaging-release + demo-dogfooding + browser-accuracy
- **Demo update** -> demo-dogfooding + development-workflow + library-architecture
- **Roadmap decision** -> priorities-roadmap + research-log + architecture-review
- **Architecture review** -> architecture-review + library-architecture + benchmarks-profiling

## Additional Package Index

- [`asset-link-index.md`](asset-link-index.md)
- [`manifest.json`](manifest.json)
