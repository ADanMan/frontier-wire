#!/usr/bin/env python3
"""Self-growing feeds: discover and technically vet RSS candidates.

Usage: python3 scripts/gardener.py
Scans source: URLs from recent editions/digests, takes domains not yet in
feeds.txt, autodiscovers their RSS (link rel=alternate + common paths), and
prints a vetted candidate report. Adding to feeds.txt stays a curated step
(editorial criteria live in .claude/skills/feed-gardener/SKILL.md).
Stdlib only; open network required (run from the operator loop, not sandbox).
"""
from __future__ import annotations
import datetime, re, sys, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "frontier-wire-gardener/1.0"}
COMMON = ["/feed", "/rss", "/feed.xml", "/rss.xml", "/atom.xml", "/index.xml", "/feed/", "/rss/"]
SKIP_DOMAINS = {"github.com", "arxiv.org", "huggingface.co", "raw.githubusercontent.com",
                "youtube.com", "twitter.com", "x.com", "reddit.com", "en.wikipedia.org"}


def get(url, timeout=12):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def known_domains():
    doms = set()
    for line in (ROOT / "feeds.txt").read_text().splitlines():
        line = line.strip()
        if line.startswith("http"):
            doms.add(urllib.parse.urlparse(line.split()[0]).netloc.removeprefix("www."))
    return doms


def recent_source_domains(days=7):
    cutoff = datetime.date.today() - datetime.timedelta(days=days)
    doms = {}
    for f in ROOT.glob("editions/*/*/*.md"):
        m = re.search(r"^source:\s*(\S+)", f.read_text(errors="ignore"), re.M)
        if not m:
            continue
        d = urllib.parse.urlparse(m.group(1)).netloc.removeprefix("www.")
        if d and d not in SKIP_DOMAINS:
            doms.setdefault(d, m.group(1))
    return doms


def parse_feed(url):
    try:
        root = ET.fromstring(get(url))
    except Exception:
        return None
    items = [e for e in root.iter() if e.tag.split("}")[-1] in ("item", "entry")]
    dates = []
    for e in items:
        for c in e:
            if c.tag.split("}")[-1] in ("pubDate", "published", "updated") and c.text:
                dates.append(c.text[:25])
                break
    return {"count": len(items), "latest": dates[0] if dates else "?"}


def discover(domain):
    base = f"https://{domain}"
    try:
        html = get(base).decode("utf-8", "ignore")
        m = re.search(r'<link[^>]+type=["\']application/(?:rss|atom)\+xml["\'][^>]*href=["\']([^"\']+)', html, re.I)
        if m:
            return urllib.parse.urljoin(base, m.group(1))
    except Exception:
        pass
    for p in COMMON:
        u = base + p
        if parse_feed(u):
            return u
    return None


def main() -> int:
    known = known_domains()
    cands = {d: u for d, u in recent_source_domains().items() if d not in known}
    if not cands:
        print("no new candidate domains this week")
        return 0
    print(f"# gardener candidates {datetime.date.today()} (tech-vetted; apply SKILL.md criteria before adding)\n")
    for d, src in sorted(cands.items()):
        feed = discover(d)
        if not feed:
            print(f"SKIP {d}  (no RSS found)  first seen via {src}")
            continue
        info = parse_feed(feed)
        ok = info and info["count"] >= 3
        print(f"{'CAND' if ok else 'WEAK'} {feed}  items={info['count'] if info else 0} latest={info['latest'] if info else '?'}  via {src}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
