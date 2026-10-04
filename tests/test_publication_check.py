import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


class PublicationCheckTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location(
            "publication_check", Path(__file__).parents[1] / "scripts/publication_check.py"
        )
        self.assertTrue(Path(spec.origin).exists(), "publication guard is missing")
        self.guard = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.guard)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.day = dt.date(2026, 10, 4)
        self.now = dt.datetime(2026, 10, 3, 22, 30, tzinfo=dt.timezone.utc)
        self.source = "https://example.org/story?utm_source=rss"
        digest = self.root / "digests/2026/2026-10-04.md"
        digest.parent.mkdir(parents=True)
        digest.write_text(f"---\ndate: 2026-10-04\n---\n  - source: {self.source}\n")
        self.folder = self.root / "editions/2026/10-04"
        self.folder.mkdir(parents=True)
        (self.folder / "index.md").write_text("---\ndate: 2026-10-04\nedition: 1\n---\n## От редакции\nДа.\n## Editorial\nYes.\n")
        self.article = self.folder / "01-story.md"
        self.article.write_text(
            "---\ndate: 2026-10-04\nrubric: science\n"
            "title_ru: История\ntitle_en: Story\ndek_ru: Текст.\ndek_en: Text.\n"
            f"source: {self.source}\ngenerated: true\n---\n"
            "## Русская версия\n" + "слово " * 350 +
            f"[источник]({self.source})\n### Почему это важно\nВывод.\n"
            "## English version\n" + "word " * 350 +
            f"[source]({self.source})\n### Why it matters\nConclusion.\n"
        )

    def check(self):
        return self.guard.check(self.root, self.day, "morning", [self.article.name], self.now)

    def test_utc_previous_day_is_current_moscow_day(self):
        self.assertEqual(self.check()["status"], "ready")

    def test_rejects_backfill_date(self):
        with self.assertRaisesRegex(ValueError, "Moscow"):
            self.guard.check(self.root, self.day - dt.timedelta(days=1), "morning", [], self.now)

    def test_rejects_source_republished_with_tracking_variation(self):
        old = self.root / "editions/2026/09-30"
        old.mkdir(parents=True)
        (old / "01-old.md").write_text("---\nsource: https://example.org/story?utm_campaign=old#top\n---\n")
        with self.assertRaisesRegex(ValueError, "already published"):
            self.check()

    def test_rejects_source_absent_from_digest(self):
        self.article.write_text(self.article.read_text().replace(self.source, "https://example.org/unknown"))
        with self.assertRaisesRegex(ValueError, "digest"):
            self.check()

    def test_same_slot_is_idempotent(self):
        result = self.check()
        self.guard.record(self.root, result)
        again = self.guard.check(self.root, self.day, "morning", [], self.now)
        self.assertEqual(again["status"], "already_recorded")
        marker = self.root / "publication_runs/2026/2026-10-04-morning.json"
        self.assertEqual(json.loads(marker.read_text())["articles"], result["articles"])

    def test_rejects_path_escape(self):
        with self.assertRaisesRegex(ValueError, "filename"):
            self.guard.check(self.root, self.day, "morning", ["../09-30/01-old.md"], self.now)

    def test_later_slot_cannot_overwrite_previous_batch(self):
        self.guard.record(self.root, self.check())
        with self.assertRaisesRegex(ValueError, "another slot"):
            self.guard.check(self.root, self.day, "evening", [self.article.name], self.now)


if __name__ == "__main__":
    unittest.main()
