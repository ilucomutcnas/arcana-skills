# Example: Checkout + filter modal edge-case triage
Matrix covered: Voice Control+iOS Safari, Switch Control+iPadOS, NVDA+Firefox 400% zoom, Windows forced colors, TalkBack+Chrome.
Failures: speech command misses unlabeled icon button; focus lost after filter apply; forced-colors removes active outline; live region floods updates.
Remediation: explicit `aria-label`, focus restore on modal close, forced-colors outline token, debounced polite announcements.
Retest checklist: command activation, switch sequential order, zoom reflow, focus persistence, announcement rate.
Acceptance: all blocking failures resolved, medium issues documented with owners and due dates.
