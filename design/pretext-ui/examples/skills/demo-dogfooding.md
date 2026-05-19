# demo-dogfooding Example

## Scenario: update `editorial-engine` demo for rich-line hint behavior

A new `lineOverflowHint` signal is added in layout output. The `pages/demos/editorial-engine.html` demo must expose the hint so contributors can evaluate whether the API is useful in real editorial flows.

## Demo States
| State | Description | Expected outcome |
|---|---|---|
| Baseline | Existing demo without hint visualization | No hint badges; current wrap behavior unchanged |
| Candidate | Hint badge + debug panel bound to `lineOverflowHint` | Hint appears only on overflow-prone lines |
| Edge case | Mixed Arabic/English paragraph at narrow width | Hint remains stable across resize and direction changes |
| Failure state | Hint appears on every line regardless of overflow | Treated as regression; block merge |

## QA Checklist
- [ ] Rich line API behavior: hint only emitted where overflow risk is computed.
- [ ] Resize behavior: hint updates correctly at 480/640/768 without stale state.
- [ ] Script-sensitive text: mixed RTL/LTR and CJK samples render with correct hint placement.
- [ ] Visual stability: no badge flicker/reflow loops during repeated resize.
- [ ] Developer-facing debug output: demo panel shows source line index + hint reason for triage.

## Feedback Loop
- Feed to **library-architecture**: confirm hint semantics and field contract are useful, not redundant.
- Feed to **priorities-roadmap**: if hint catches recurring regressions, prioritize tooling around hint diagnostics.
- Feed to **browser-accuracy**: use demo mismatch captures as targeted repro seeds for cross-browser sweeps.

## Acceptance Criteria
- Demo validates a real API need (reviewers can identify overflow-risk lines faster), not ornamental UI.
- Regression evidence (before/after state + targeted checks) is attached.
- Follow-up owner/action is recorded for any unresolved edge-case behavior.
