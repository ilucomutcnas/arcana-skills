# library-architecture Example

## Concrete Change Request
Add `lineOverflowHint` metadata emitted by `layout`, consumed by diagnostic pages (`pages/accuracy.html`, `pages/corpus.html` pathways), while preserving compatibility for consumers that do not read the new field.

## Compatibility Expectations
- Field is optional and additive.
- Existing consumers parsing layout output without `lineOverflowHint` continue to work.
- No renaming/removal of existing layout metadata fields.

## API Impact Table
| Surface | Public/Internal | Impact | Migration needed | Risk |
|---|---|---|---|---|
| `layout` output object | Public | Add optional `lineOverflowHint` | No (optional) | Medium: API widening |
| `analyze` summary | Internal-facing report output | Aggregate hint counts | No, but docs update | Low |
| diagnostic pages data adapter | Internal | Read hint for UI diagnostics | Minor adapter update | Low |
| downstream strict schema consumers | Public ecosystem | May reject unknown fields if schema locked | Possibly (schema relax) | Medium |

## Responsibility Map
- `prepare`: preserve input normalization; no behavior change in token preparation.
- `layout`: compute `lineOverflowHint` at the measurement/line-break boundary where final break candidate is chosen.
- `analyze`: consume optional hint and emit aggregate diagnostics.
- Measurement/line-break boundary: measurement provides widths; line-break decides boundary; hint must represent that boundary decision without re-measuring.

## Risk Review
- **Public API widening**: additive field can still break strict validators; call out compatibility note.
- **Hot path cost**: hint computation must not add measurable overhead on dense corpora.
- **Browser accuracy**: hint must not mask real wrap divergence; cross-browser evidence required.
- **Corpus/canary impact**: Arabic and mixed corpora must show stable behavior after field addition.

## Acceptance Criteria
- Optional field does not break existing consumers in package smoke checks.
- Browser and corpus evidence exists for representative samples/widths.
- `architecture-review` signoff is captured because public API surface changes.
