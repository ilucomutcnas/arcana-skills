# Routing Guide

## Shared Rules
- Start from the narrowest primary mini-skill.
- Add adjacent + validation mini-skills for non-trivial tasks.
- Use `shared-rules/ANTI-PATTERNS.md` to reject unsafe shortcuts.

## Quick Navigation
- Core engine: `library-architecture`
- Contributor loop: `development-workflow`
- Accuracy: `browser-accuracy`
- Performance: `benchmarks-profiling`
- Corpus diagnostics: `corpus-diagnostics`
- Release: `packaging-release`
- Demo QA: `demo-dogfooding`
- Prioritization: `priorities-roadmap`
- Historical evidence: `research-log`
- Escalated review: `architecture-review`

## Routing Scenarios
- **Public API changes** -> library-architecture + corpus-diagnostics + architecture-review
- **Layout mismatch in page/demo** -> browser-accuracy + library-architecture + corpus-diagnostics
- **Browser sweep** -> browser-accuracy + development-workflow + corpus-diagnostics
- **Performance regression** -> benchmarks-profiling + library-architecture + architecture-review
- **Corpus/canary update** -> corpus-diagnostics + browser-accuracy + research-log
- **Release candidate** -> packaging-release + demo-dogfooding + browser-accuracy
- **Demo update** -> demo-dogfooding + development-workflow + library-architecture
- **Roadmap decision** -> priorities-roadmap + research-log + architecture-review
- **Architecture review** -> architecture-review + library-architecture + benchmarks-profiling

## Additional Package Index
- [`asset-link-index.md`](asset-link-index.md)
- [`manifest.json`](manifest.json)
