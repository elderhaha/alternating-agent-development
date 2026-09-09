"""Install one shared protocol and selected thin agent adapters (Python 3.10+)."""
import argparse
import hashlib
from pathlib import Path
import shutil

NAME = 'alternating-agent-development'
VERSION = '1.0.0'
ROOT = Path(__file__).resolve().parent


def install(home, agents, replace=False, dry_run=False):
    home = home.expanduser().resolve()
    shared = home / '.agents' / 'protocols' / NAME
    release = Path('releases') / VERSION / NAME
    source = ROOT / release
    entries = {'codex': home / '.agents/skills' / NAME / 'SKILL.md',
               'claude': home / '.claude/skills' / NAME / 'SKILL.md'}
    writes = {shared / release / f.relative_to(source): f.read_bytes()
              for f in source.rglob('*') if f.is_file()}
    for agent in agents:
        template = (ROOT / 'adapters' / agent / NAME / 'SKILL.md').read_text(encoding='utf-8')
        writes[entries[agent]] = template.replace('@PROTOCOL_PATH@',
            (shared / release / 'SKILL.md').as_posix()).encode('utf-8')
    # Preflight all writes before changing any file. Never silently rewrite a release.
    for target, data in writes.items():
        if not target.resolve().is_relative_to(home):
            raise ValueError(f'Target escapes selected home: {target}')
        if target.exists() and target.read_bytes() != data:
            if target not in entries.values() or not replace:
                raise ValueError(f'Conflicting file: {target}; adapter replacement requires --replace-adapter')
    for target, data in writes.items():
        print(('Would install: ' if dry_run else 'Install: ') + str(target))
        if dry_run:
            continue
        if target.exists() and target.read_bytes() != data:
            digest = hashlib.sha256(target.read_bytes()).hexdigest()[:12]
            backup = shared / 'backups' / (target.parent.parent.parent.name + '-' + digest + '.md')
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(target, backup)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    if not dry_run:
        print('Installed. Open a fresh agent session. Existing project version pins are unchanged.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=['codex', 'claude', 'both'], default='both')
    parser.add_argument('--home', type=Path, default=Path.home(), help='Target user home; also useful for isolated validation')
    parser.add_argument('--replace-adapter', action='store_true', help='Back up and replace a different existing adapter')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        install(args.home, ['codex', 'claude'] if args.agent == 'both' else [args.agent],
                args.replace_adapter, args.dry_run)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')
