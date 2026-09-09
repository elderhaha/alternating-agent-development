# Checkpoints and closeout

## Small checkpoint

After a meaningful unit, update the mapped current record with goal/unit, actual change, verification basis/results,
remaining issue and next step. A tiny typo need not trigger a separate record. Suggested ID: H001.c01 (not software version).
Use an existing equivalent ID scheme if present. No mandatory commit or tag for each small checkpoint.

## Full handoff

On tool switch, end of a work round or user request, consolidate the latest full record and its deltas into a new full record
(e.g. H002). Absorb outstanding facts, authorization and risks even when unchanged. Keep the active record concise;
details and evidence can be linked but crucial recovery instructions must be directly present.
Old deltas become historical, not a parallel current source. Preserve them through Git or the existing history carrier
before replacing unsaved material. Do not delete uncommitted unique information during consolidation.

Include objective, authorization categories, completed/unfinished status, tests (including not-run and unknown), decisions
with reasons/reconsideration conditions, risks, files and references, branch/HEAD/worktree/untracked state, and executable
next units with dependency and success condition. Record phase separately from outcome.

Git snapshot should describe the implementation base and the diff/working-tree context at recording time, not claim the
record's future enclosing commit hash. After committing, verify the final state and identify the enclosing commit in the
delivery; the next agent can find it through Git. Avoid self-referential commit updates in an endless loop.

## Quota / emergency

Immediately freeze expansion and write a minimum recovery note: goal + authorization, branch/base, files being changed,
partial location or failure, last actual verification and first recovery action. Do this before attempting closure.
If time allows, close the smallest safe unit, run critical checks and upgrade the note to a full handoff.
If not, mark partial/unverified with exact gaps. Do not start cleanup, refactoring or dependency repair simply to make
the worktree look clean. Never erase user work; neither stash nor destructive rollback is a default handoff action.
No reliable quota signal is necessary: user requests take effect immediately. Abrupt termination can happen before a final
note, so small checkpoints reduce loss; the skill cannot guarantee recovery of information never written down.

## Risk supplement

For materially risky work, add the relevant invariants and affected data/API scope, evidence tied to the tested state,
unverified boundaries, recovery/rollback constraints and any still-required operational authorization. Risk is independent
of checkpoint size. Do not run production writes, irreversible migrations, releases or external messages because a
handoff recommends them; preserve the user's actual authorization boundary.
