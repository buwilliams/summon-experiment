import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from summon.storage import FileStore, segment


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = FileStore(self.root / "files")
        self.catalog = dict(id="catalog", revision=1, scenarios=[dict(id="s", name="A scenario", text="Unicode — café")], views=[])

    def tearDown(self):
        self.temp.cleanup()

    def test_revisions_readability_and_reload(self):
        self.store.put("catalog", self.catalog)
        newer = {**self.catalog, "revision": 2}
        self.store.put("catalog", newer)
        self.assertEqual(len(list((self.store.path / "catalog").glob("*.json"))), 2)
        self.assertIn("Unicode — café", (self.store.path / "catalog/revision-000001.md").read_text(encoding="utf-8"))
        self.assertEqual(FileStore(self.store.path).get("catalog", "catalog"), newer)

    def test_recovery_after_interrupted_write(self):
        original = self.store._atomic
        def fail_markdown(path, text):
            if path.suffix == ".md":
                raise OSError("Simulated disk interruption")
            return original(path, text)
        self.store._atomic = fail_markdown
        with self.assertRaises(OSError):
            self.store.put("catalog", self.catalog)
        self.assertTrue((self.store.path / ".pending.json").exists())
        recovered = FileStore(self.store.path)
        self.assertEqual(recovered.get("catalog", "catalog"), self.catalog)
        self.assertTrue((self.store.path / "catalog/revision-000001.md").exists())
        self.assertFalse((self.store.path / ".pending.json").exists())

    def test_sqlite_migration_retains_source_and_runs_once(self):
        legacy = self.root / "legacy.sqlite3"
        with sqlite3.connect(legacy) as db:
            db.execute("CREATE TABLE records (kind TEXT, id TEXT, body TEXT)")
            db.execute("INSERT INTO records VALUES (?,?,?)", ("catalog", "catalog", json.dumps(self.catalog)))
        db.close()
        before = legacy.read_bytes()
        self.store.migrate_sqlite(legacy)
        self.assertEqual(self.store.get("catalog", "catalog"), self.catalog)
        self.assertEqual(legacy.read_bytes(), before)
        newer = {**self.catalog, "revision": 2}
        self.store.put("catalog", newer)
        self.store.migrate_sqlite(legacy)
        self.assertEqual(self.store.get("catalog", "catalog"), newer)

    def test_paths_are_safe_and_distinct(self):
        name = "../../CON/Unsafe: name?"
        self.assertNotIn("/", segment(name, "one"))
        self.assertNotIn("..", segment(name, "one"))
        self.assertNotEqual(segment(name, "one"), segment(name, "two"))


if __name__ == "__main__":
    unittest.main()
