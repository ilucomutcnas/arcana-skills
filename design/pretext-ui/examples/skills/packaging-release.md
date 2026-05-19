# packaging-release Example

## Scenario: prepare release candidate for Pretext package

A release candidate includes line-layout metadata changes and demo updates. Maintainer must verify package shape and release confidence before publishing.

## Package Export Table
| Export | Path | Status | Notes |
|---|---|---|---|
| `.` | `dist/index.js` | pass | main API unchanged |
| `./analysis` | `dist/analysis.js` | pass | diagnostics helper preserved |
| `./layout` | `dist/layout.js` | pass | includes metadata update |
| `./package.json` | `package.json` | pass | export map consistent |

## Dist/Entrypoint Checks
- Dist contains expected JS + type declaration files.
- Export map resolves in Node ESM and bundler smoke harness.
- No orphaned build artifacts from previous release.

## Smoke Test Checklist
- [ ] Consumer import smoke test passes.
- [ ] Minimal layout render scenario runs.
- [ ] Browser accuracy snapshots verified for release candidate.
- [ ] Benchmark budget not exceeded for mixed-script suite.
- [ ] Demo pages load without runtime export errors.

## Release-Blocker Table
| Blocker | Gate | Outcome |
|---|---|---|
| Export mismatch | package-smoke-test | none |
| Dist missing declaration | build check | none |
| Browser regression | accuracy sweep | none |
| Perf regression > budget | benchmark check | none |

## Go / No-Go Decision
- **Go**: all package/export/smoke gates pass, no blocking browser or perf deltas.
- **No-Go**: any export resolution error or benchmark/browsers fail; fix-forward only for non-blocking docs wording.
