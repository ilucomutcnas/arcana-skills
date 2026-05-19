# architecture-review Example

## Scenario: Arabic cache-heavy diff touching layout + packaging

A contributor proposes a diff that introduces cached shaping fragments for Arabic paragraphs and also updates package exports to expose a new diagnostics helper. Review must decide whether to approve, request changes, or block release.

## Scope Snapshot
- Affected modules: `src/layout.ts`, `src/bidi.ts`, `src/analysis.ts`, `scripts/corpus-sweep.ts`, `resources/manifest.json` consumers.
- Corpus stress set: `corpora/ar-al-bukhala.txt`, `corpora/ar-risalat-al-ghufran-part-1.txt`, and `corpora/mixed-app-text.txt`.
- Risk surface: reorder bugs in bidi runs, stale cache invalidation, export compatibility drift.

## Risk Table
| Risk | Severity | Signal | Required Mitigation |
|---|---|---|---|
| Cached shaping returns stale glyph metrics | High | Wrap shifts after width changes | Cache key includes width/font/script and invalidates on measurement inputs |
| Bidi run ordering regression for Arabic + Latin inline spans | High | Logical and visual order diverge in corpus probes | Cross-browser corpus sweep with mismatch taxonomy attached |
| New export breaks consumers using strict ESM imports | Medium | Package smoke test fails on entrypoint resolution | Entrypoint/export table and smoke logs for Node + bundler |
| Corpus diagnostics script no longer matches layout metadata schema | Medium | Extractor throws missing field | Migration note and fallback parser path |

## Evidence Requirements (Cross-skill)
- From `library-architecture`: API impact boundary and responsibility map (`prepare/layout/analyze`) with compatibility note.
- From `browser-accuracy`: Chromium/Firefox/WebKit sweep showing no blocking wrap-order deltas for Arabic canaries.
- From `corpus-diagnostics`: width matrix (480/640/768) with taxonomy tags for any residual mismatch.

## Reviewer Comments
### Approval comment (if evidence is complete)
> Cache invalidation keys now include width + script + font fallback chain, and Arabic canaries are stable across three engines. Export addition is backward compatible; smoke tests confirm unchanged existing entrypoints.

### Blocking comment (if evidence is incomplete)
> Block: no Firefox evidence for Arabic mixed-direction paragraphs and no migration note for diagnostics schema change. Provide corpus taxonomy output and compatibility statement before merge.

## Final Recommendation
- **Approve with conditions** when all three evidence streams are attached and package smoke tests pass.
- **Block** if any API boundary, browser parity, or corpus matrix artifact is missing.
- **Escalate** to architecture-review follow-up if cache logic adds global mutable state not covered by deterministic test cases.
