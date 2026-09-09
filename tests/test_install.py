import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
import re

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)

    def run_install(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(self.home, ['codex', 'claude'], **kwargs)

    def test_both_entries_resolve_one_release_and_no_duplicates(self):
        self.run_install()
        self.run_install()
        shared = self.home / '.agents/protocols' / installer.NAME
        for tool in ['.agents', '.claude']:
            found = list((self.home / tool / 'skills').rglob('SKILL.md'))
            self.assertEqual(len(found), 1)
            self.assertIn(shared.as_posix(), found[0].read_text(encoding='utf-8'))
            self.assertNotIn('@PROTOCOL_PATH@', found[0].read_text(encoding='utf-8'))
        for f in (ROOT / 'releases').rglob('*'):
            if f.is_file():
                self.assertEqual(f.read_bytes(), (shared / f.relative_to(ROOT)).read_bytes())
        for f in (shared / 'releases').rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)', f.read_text(encoding='utf-8')):
                self.assertTrue((f.parent / link).is_file(), link)

    def test_dry_run_writes_nothing(self):
        self.run_install(dry_run=True)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_adapter_conflict_is_protected_then_backed_up(self):
        entry = self.home / '.claude/skills' / installer.NAME / 'SKILL.md'
        entry.parent.mkdir(parents=True)
        entry.write_text('original')
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertFalse((self.home / '.agents').exists())
        self.run_install(replace=True)
        backups = list((self.home / '.agents/protocols' / installer.NAME / 'backups').glob('*.md'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), 'original')

    def test_release_conflict_is_never_overwritten(self):
        self.run_install()
        entry = self.home / '.agents/protocols' / installer.NAME / 'releases/1.0.0' / installer.NAME / 'SKILL.md'
        entry.write_text('changed release')
        with self.assertRaises(ValueError):
            self.run_install(replace=True)
        self.assertEqual(entry.read_text(), 'changed release')

    def test_single_agent_does_not_install_other_entry(self):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(self.home, ['claude'])
        self.assertFalse((self.home / '.agents/skills').exists())
        self.assertTrue((self.home / '.claude/skills' / installer.NAME / 'SKILL.md').exists())


if __name__ == '__main__':
    unittest.main()
