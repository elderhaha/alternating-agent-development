# Adoption and project mapping

Read existing agent instructions before edits. Inventory only relevant instruction, status, architecture, decision,
testing, work log, roadmap and Git workflow files. Inspect repository root, worktree and recent changes.
Report reusable responsibilities, overlaps, missing coverage and conflicts; present a concrete minimal integration plan
before modifying. Existing user authorization to implement is sufficient; do not add an approval ceremony.

Choose one current record and one mapping. Reuse sections where they already serve the purpose.
If absent, defaults are: root AGENTS.md for shared entry, CLAUDE.md as thin reference, a project mapping section
in the development guide (or a new small agent-workflow.md), and CURRENT_WORK.md for current state.
Decisions live in relevant architecture/design documents; create a decision log only if no suitable carrier exists.
File names are defaults, not prescribed project structure. Maps should use repository-relative references.

The mapping must identify: protocol version/location, primary business/engineering instructions, current record,
architecture, decision home, tests/environment, work history, roadmap/authorization source, Git policy and agent entries.
For a genuinely new project these fields may be explicitly absent; establish goal and validation before implementation.
If the project is not a Git repository, record that fact and available file snapshots; do not invent commits or initialize
Git without task authorization. Missing approved goal is not permission to execute suggestions.

Align conflicting legacy continuity habits (e.g. always read all logs, tag every session) with the protocol.
Do not override business constraints or platform instructions. Resolve documented precedence directly; report only
material unresolved conflicts requiring a user decision, continuing unaffected authorized work.

Pin the release in each mapping. An installed adapter's default applies only when no project pin exists.
Missing/unreadable pinned protocol: identify the missing dependency and preserve recoverable state; do not silently
substitute a different version. A new tool can follow the repository entry even without native skill installation.

The canonical protocol release is tool- and project-independent. Tool paths and discovery instructions belong in adapters;
business tests, domains and secrets never belong in the protocol. Upgrades are explicit: new release, scenario validation,
mapping migration, adapter default update. Do not mutate an adopted released version's semantics in place.
