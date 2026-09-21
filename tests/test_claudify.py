import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import claudify


class ClaudifyTests(unittest.TestCase):
    def test_safe_name(self):
        self.assertEqual(claudify.safe_name("My Club Night!"), "my-club-night")

    def test_available_examples(self):
        examples = claudify.available_examples()
        self.assertIn("event-announcement-pack", examples)
        self.assertIn("window-display-loop", examples)
        self.assertEqual(len(examples), 5)

    def test_create_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = claudify.create_project("My Event", "post-event-clip-harvest", Path(tmp))
            self.assertTrue((project / "CLAUDE.md").exists())
            self.assertTrue((project / "PROJECT_BRIEF.md").exists())
            self.assertTrue((project / "CONSENT_LEDGER.md").exists())
            text = (project / "PROJECT_BRIEF.md").read_text(encoding="utf-8")
            self.assertIn("Post-Event Clip Harvest", text)

    def test_refuses_non_empty_existing_project_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "my-event"
            project.mkdir()
            (project / "keep.md").write_text("do not overwrite", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                claudify.create_project("My Event", "event-announcement-pack", Path(tmp))


if __name__ == "__main__":
    unittest.main()
