#!/usr/bin/env python3
"""Check one current Moscow-day batch; optionally record it for scheduler retries.

No network, model, credentials, scheduler, commit or push. The editor still checks
the full sources and builds/publishes through the existing repository workflow.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
MOSCOW = ZoneInfo("Europe/Moscow")
SLOTS = ("morning", "evening", "recovery")
TRACKING = {"fbclid", "gclid", "at_medium", "at_campaign", "traffic_source"}


def canonical(url):
    parsed = urlsplit(url.strip())
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("source must be an HTTP(S) URL")
    query = sorted((k, v) for k, v in parse_qsl(parsed.query)
                   if not k.lower().startswith("utm_") and k.lower() not in TRACKING)
    return urlunsplit(("https", parsed.netloc.lower(), parsed.path.rstrip("/"), urlencode(query), ""))


def meta(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or len(text.split("---", 2)) != 3:
        raise ValueError(f"missing front matter: {path.name}")
    return dict(line.split(":", 1) for line in text.split("---", 2)[1].splitlines()
                if ":" in line)


def fields(path):
    return {k.strip(): v.strip().strip("\"'") for k, v in meta(path).items()}


def checksum(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def marker_path(root, day, slot):
    return root / "publication_runs" / str(day.year) / f"{day}-{slot}.json"


def check(root, day, slot, names, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    if day != now.astimezone(MOSCOW).date():
        raise ValueError("only the current Moscow date may be published; no backfill")
    if slot not in SLOTS:
        raise ValueError("unknown publication slot")
    marker = marker_path(root, day, slot)
    if marker.exists():
        result = json.loads(marker.read_text())
        for item in result["articles"]:
            if checksum(root / item["path"]) != item["sha256"]:
                raise ValueError("recorded article changed; inspect before retrying")
        return dict(result, status="already_recorded")
    if not 1 <= len(names) <= 8 or len(set(names)) != len(names):
        raise ValueError("choose 1–8 distinct new article filenames")
    if any(not re.fullmatch(r"\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md", n) for n in names):
        raise ValueError("article filename must be NN-kebab-slug.md without directories")
    digest = root / "digests" / str(day.year) / f"{day}.md"
    if not digest.exists() or fields(digest).get("date") != str(day):
        raise ValueError("a digest for the current Moscow date is required")
    allowed = {canonical(u) for u in re.findall(r"^\s*- source: (\S+)", digest.read_text(), re.M)}
    folder = root / "editions" / str(day.year) / day.strftime("%m-%d")
    cover = fields(folder / "index.md")
    if cover.get("date") != str(day) or not cover.get("edition", "").isdigit():
        raise ValueError("cover date/edition is invalid")
    selected = {folder / n for n in names}
    for existing in (root / "publication_runs").rglob("*.json"):
        batch = json.loads(existing.read_text())
        if any(root / item["path"] in selected for item in batch["articles"]):
            raise ValueError("article already recorded in another slot; append new filenames")
    previous = set()
    for p in (root / "editions").rglob("*.md"):
        if p.name == "index.md" or p in selected:
            continue
        source = fields(p).get("source")
        if source:
            previous.add(canonical(source))
    records = []
    seen = set()
    for p in sorted(selected):
        data = fields(p)
        required = ("title_ru", "title_en", "dek_ru", "dek_en", "source")
        if any(not data.get(k) for k in required) or data.get("date") != str(day):
            raise ValueError(f"missing metadata or wrong date: {p.name}")
        if data.get("rubric") not in {"ai", "tech", "science", "world", "culture", "economy"}:
            raise ValueError(f"invalid rubric: {p.name}")
        if data.get("generated") != "true":
            raise ValueError(f"generated flag is required: {p.name}")
        source = canonical(data["source"])
        if source not in allowed:
            raise ValueError(f"source absent from today's digest: {p.name}")
        if source in previous or source in seen:
            raise ValueError(f"source already published: {p.name}")
        seen.add(source)
        body = p.read_text().split("---", 2)[2]
        if "## Русская версия" not in body or "## English version" not in body:
            raise ValueError(f"both language sections are required: {p.name}")
        ru, en = body.split("## English version", 1)
        ru = ru.split("## Русская версия", 1)[1]
        for language, section, ending in (("RU", ru, "### Почему это важно"), ("EN", en, "### Why it matters")):
            words = re.findall(r"\S+", re.sub(r"\]\([^)]*\)", "]", section))
            if not 350 <= len(words) <= 550 or ending not in section:
                raise ValueError(f"{language} must contain 350–550 words and its ending: {p.name} ({len(words)})")
            if data["source"] not in section:
                raise ValueError(f"inline source link required in {language}: {p.name}")
        records.append({"path": str(p.relative_to(root)), "sha256": checksum(p), "source": source})
    return {"status": "ready", "date": str(day), "slot": slot,
            "checked_at": now.isoformat(), "digest_sha256": checksum(digest), "articles": records}


def record(root, result):
    marker = marker_path(root, dt.date.fromisoformat(result["date"]), result["slot"])
    marker.parent.mkdir(parents=True, exist_ok=True)
    with marker.open("x", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slot", required=True, choices=SLOTS)
    parser.add_argument("--date", type=dt.date.fromisoformat, default=dt.datetime.now(MOSCOW).date())
    parser.add_argument("--record", action="store_true")
    parser.add_argument("articles", nargs="*")
    args = parser.parse_args()
    try:
        result = check(ROOT, args.date, args.slot, args.articles)
        if args.record and result["status"] == "ready":
            record(ROOT, result)
        print(json.dumps(result, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        print(f"Publication check failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
