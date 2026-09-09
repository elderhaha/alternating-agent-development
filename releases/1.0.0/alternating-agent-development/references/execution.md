# Intake, takeover and review

1. Read mapped authority, full handoff and only its later small checkpoints; load relevant design/decisions on demand.
2. Inspect repository root, branch, HEAD, worktree path, tracked diff and untracked files. Distinguish changes recorded by
   the prior agent from unrelated work; uncertain ownership is not permission to overwrite. Inspect pertinent code/tests.
3. Check record freshness against that state. A matching commit alone does not validate dirty changes. Check external
   state only where relevant and authorized, recording evidence locations rather than secrets or full datasets.
4. If consistent, continue the next authorized dependency-ready unit. Do not repeat planning, all tests or completed work.
   If inconsistent, isolate the discrepancy, perform targeted verification, correct the current record and continue.
   Prior decisions stand until new evidence, a documented reconsideration condition or user direction justifies changing them.

For medium or larger tasks, define outcome, scope/exclusions, acceptance, test method, dependencies and a recoverable
checkpoint. PASS if the unit is tractable; DECOMPOSE if too broad; BLOCKED if a necessary dependency/decision is missing.
Do not pretend to know a session's capacity. Prefer a conservative verifiable unit, leaving room to record state.
“Add a failing test, fix behavior, run the relevant checks” normally belongs to one result-oriented unit.

Validate according to impact and project requirements: documentation may need links and diff checks; behavior needs
relevant tests; migrations need isolated representative data, invariants, compatibility and a recovery strategy.
No requirement to run the full suite on every checkpoint. If code changes after a run, identify the untested delta.
Missing dependencies or credentials: state which checks did not run and why; no fabricated PASS or scope-expanding repair.

High-risk review is a role, not a fixed model assignment. Findings need evidence, consequence and actionable scope.
Stylistic preference alone does not justify rewriting correct work. Resolve concrete findings and perform necessary checks;
end when acceptance is met, or record a remaining blocker instead of cycling through reviews indefinitely.

Review findings and roadmap items are proposals until covered by the user's existing authorization. Continuing an already
approved unit does not require reapproval. A business choice or genuinely new scope needs user direction.
