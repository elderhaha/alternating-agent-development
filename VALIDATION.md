# Validation and limits

## Protocol 1.0.0

The release files are unchanged from the privately developed protocol. This repository publishes only the reusable workflow, not the source project's data, conversations, handoffs or business rules.

Maintainer-observed trials on Windows included:

- A fresh Claude Code session locating instructions and reporting project state without old chat context.
- Claude implementing isolated regression tests, followed by a fresh Codex review and targeted test execution.
- A user-triggered quota handoff after core implementation was already complete; the receiver preserved an unfinished browser acceptance check when access was blocked.
- Independent installation checks reporting one Claude entry and matching hashes from an unrelated project directory.

These are limited manual trials, not controlled comparative benchmarks. The implementation task prompt explicitly repeated several workflow requirements, so that trial cannot prove those behaviors arose from the skill alone. Recovery from genuinely half-written code was not demonstrated. Emergency, stale-record and high-risk cases also received written scenario walkthroughs; walkthroughs are not live behavioral proof.

## Public package checks

The automated tests exercise installation into temporary homes, both agent targets, repeat installation, protected conflicts, explicit adapter replacement with backup, dry-run behavior, release integrity and resource links. They do not run either coding agent or prove natural-language activation.

Known limits:

- No token telemetry, automatic session transfer or background capture.
- Abrupt termination can lose work not saved in checkpoints.
- Project mappings must point to an installed, readable release.
- Other tools and operating systems require their own live validation.
- User-level installation does not transfer project authorization or credentials.
