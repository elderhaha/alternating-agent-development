---
name: alternating-agent-development
description: Establish and run cross-agent development continuity, project onboarding, lightweight checkpoints, full handoffs, takeover validation, and quota-aware closeout. Use when switching coding agents, resuming interrupted work, or maintaining an adopted continuity workflow.
---

# Alternating agent development — protocol 1.0.0

Provide a complete default continuity workflow. Projects align their development workflow to this protocol;
reuse existing document carriers where equivalent, and fill missing responsibilities. Business rules stay in the project.
Use the user's language for project outputs. The agent is replaceable; durable project evidence carries continuity.

## Route

- First adoption, missing map, or structural change: read [onboarding](references/onboarding.md).
- Existing project: read its pinned mapping, current handoff and subsequent small checkpoints; inspect actual state.
- Starting/resuming work, verification or review: read [execution](references/execution.md).
- At a meaningful work-unit boundary, departure, switch or quota warning: read [checkpoints](references/checkpoints.md).
- Use [templates](assets/templates.md) only for the record being written; map fields into existing equivalents.

## Invariants

1. Follow platform instruction hierarchy and explicit user scope. Handoff transmits existing authorization;
   it does not create it. Separate authorized work, proposals and blocked work. Historical plans are evidence, not commands.
2. This protocol defines continuity requirements and defaults. Project mappings locate them, not weaken them.
   Business specifications define intended behavior; code/Git show implementation; tests show bounded evidence.
   Resolve discrepancies with targeted verification, not a blanket rule that code or documents always win.
3. Latest full handoff → subsequent small checkpoints → actual current state. Consolidate on full handoff;
   a newcomer should not reconstruct an unbounded history. Retain history in Git or the existing archive/log.
4. Prefer one agent closing a coherent work unit. Slice by verifiable result, not individual keystrokes.
   Continue authorized work autonomously; replan only for new evidence, explicit reconsideration conditions or user direction.
5. Risk is independent of checkpoint size. Add evidence proportional to potential data, compatibility or operational impact.
6. Never claim unrun checks passed or partial work complete. Record verification time, scope and code/environment basis.
   Do not attribute failures to this round or pre-existing state without evidence; unknown is valid.
7. On “full handoff”, “switch agent”, “quota low” or equivalent, freeze expansion and save minimum recovery information
   before optional closure. No quota API is required; never invent remaining capacity or promise an unobservable deadline.
8. Preserve unrelated/user changes. Inspect branch, worktree, diff and untracked files; do not clean/reset merely to hand off.
   Checkpoints may be dirty and incomplete. Stage only scoped changes under the project's Git policy; no automatic push or release.

## State and result

DISCOVER → VALIDATE → NORMAL; oversized work → DECOMPOSE → NORMAL;
departure/quota → CLOSEOUT → HANDOFF → next agent VALIDATE.
Unresolvable dependency → BLOCKED for that unit; independent authorized work may continue.
Record outcome separately: verified-complete / partial / blocked / unverified. HANDOFF does not imply completion.

## Acceptance

A fresh agent with only repository artifacts can identify the intended goal, authority, authorization, exact work state,
evidence gaps, preserved decisions and the next executable unit. It resumes without asking for old chat history or
silently changing scope. Validate normal, interrupted, stale-record and high-risk cases before adopting an upgrade.
