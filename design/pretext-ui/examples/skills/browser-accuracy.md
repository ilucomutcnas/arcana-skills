# browser-accuracy Example

## Scenario: 640px wrap mismatch (Chromium diverges, Firefox/WebKit align)

During a release-candidate sweep, `pages/demos/editorial-engine.html` shows a paragraph break mismatch at width 640px. Firefox and WebKit wrap the second line after “metadata”, while Chromium pushes “metadata hint” to the next line.

## Inputs
- Diagnostic page: `pages/demos/editorial-engine.html`
- Text sample: paragraph derived from `corpora/mixed-app-text.txt` with Arabic + English inline spans
- Width: `640px`
- Browser set: Chromium, Firefox, WebKit

## Mismatch Table
| Browser | Observed wrap | Expected wrap | Severity | Suspected layer | Decision |
|---|---|---|---|---|---|
| Chromium | Breaks before `metadata` | Keep `metadata` on line 2 | High | measurement or line-break threshold | Investigate and fix candidate |
| Firefox | Keeps `metadata` on line 2 | Same as baseline | Pass | none | Keep baseline |
| WebKit | Keeps `metadata` on line 2 | Same as baseline | Pass | none | Keep baseline |

## Diagnosis Steps
1. **Reproduce** with the same page, text seed, and width in all three engines.
2. **Isolate layer**:
   - compare token measurements across engines (`measurement` suspicion),
   - verify line-break candidate ordering (`line-break` suspicion),
   - inspect bidi/inline-flow segment boundaries for mixed-direction spans.
3. **Compare with corpus diagnostics** by running corpus sweep on the same sample family (`mixed-app-text`, Arabic canary) at 640px to detect whether mismatch is page-only or corpus-wide.
4. **Decide fix / accept / refresh** based on whether the divergence changes semantic wrapping behavior or only cosmetic spacing.

## Final Decision Rules
- **Fix engine contract** when divergence changes break position or text order for representative corpus cases.
- **Refresh snapshot** only when behavior is intentional, documented, and equivalent across acceptance criteria except for non-blocking cosmetic deltas.
- **Block merge** when browser evidence is missing, mismatch severity is high, or root cause remains unassigned.

## Acceptance Criteria
- Fresh Chromium/Firefox/WebKit evidence is attached for the exact page, sample, and width.
- No unsupported claim like “browser parity is fine” without mismatch table + diagnosis notes.
- If snapshot refresh is chosen, rationale explicitly explains why no engine contract fix is required.
