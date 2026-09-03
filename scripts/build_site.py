#!/usr/bin/env python3
"""Render editions/ into a static site in docs/ (GitHub Pages).

Usage:
    python3 scripts/build_site.py

Stdlib only - the cloud routine's sandbox has no pip. Idempotent: rebuilds
docs/ from scratch on every run (assets are copied from docs_src/).
"""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EDITIONS = ROOT / "editions"
DOCS = ROOT / "docs"
SRC = ROOT / "docs_src"

RUBRICS = {
    "ai": ("AI", "ИИ"),
    "tech": ("Tech", "Технологии"),
    "science": ("Science", "Наука"),
    "world": ("World", "Мир"),
    "culture": ("Culture", "Культура"),
}

SITE_NAME = "frontier-wire"
REPO_URL = "https://github.com/ADanMan/frontier-wire"
AUTHOR_URL = "https://adanman.github.io"


def _inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1" loading="lazy">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def md_to_html(md: str) -> str:
    out: list[str] = []
    in_list = in_code = False
    for line in md.splitlines():
        if line.strip().startswith("```"):
            out.append("</code></pre>" if in_code else "<pre><code>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        s = line.strip()
        if s.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{_inline(s[2:])}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if not s:
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_inline(m.group(2))}</h{lvl}>")
        elif s.startswith("> "):
            out.append(f"<blockquote><p>{_inline(s[2:])}</p></blockquote>")
        else:
            out.append(f"<p>{_inline(s)}</p>")
    if in_list:
        out.append("</ul>")
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def parse_md(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip("'\"")
            body = parts[2]
    return meta, body.strip()


def _split_on(body: str, ru_pat: str, en_pat: str) -> tuple[str, str]:
    ru = en = ""
    cur = None
    for line in body.splitlines():
        if re.match(ru_pat, line):
            cur = "ru"
            continue
        if re.match(en_pat, line):
            cur = "en"
            continue
        if cur == "ru":
            ru += line + "\n"
        elif cur == "en":
            en += line + "\n"
    return ru.strip(), en.strip()


def split_langs(body: str) -> tuple[str, str]:
    return _split_on(body, r"^##\s+Рус", r"^##\s+English")


def split_cover(body: str) -> tuple[str, str]:
    return _split_on(body, r"^##\s+От редакции", r"^##\s+Editorial")


def page(title: str, content: str, depth: int, desc: str = "") -> str:
    p = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc or 'frontier-wire - an openly automated bilingual news wire.')}">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&display=swap">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<div class="loader" id="loader" aria-hidden="true"><span></span><span></span><span></span></div>
<header class="masthead">
  <a class="brand" href="{p}index.html"><img class="logo" src="{p}assets/logo.svg" alt="">FRONTIER<span>&mdash;</span>WIRE</a>
  <nav>
    <a href="{p}archive.html" class="nav-link"><span class="lang-ru">Архив</span><span class="lang-en">Archive</span></a>
    <a href="{REPO_URL}" class="nav-link">GitHub</a>
    <button id="langToggle" class="lang-toggle" aria-label="Switch language">EN</button>
  </nav>
</header>
<main>
{content}
</main>
<footer>
  <p class="lang-ru">Издание собирает и печатает открыто автоматизированная рутина &mdash; дважды в день, из настоящих источников. Издатель: <a href="{AUTHOR_URL}">Данила Катальшов</a> &middot; <a href="https://t.me/adanman">Telegram</a> &middot; <a href="https://www.linkedin.com/in/danilakatalshov">LinkedIn</a></p>
  <p class="lang-en">This paper is written and shipped by an openly automated routine &mdash; twice a day, from real sources. Publisher: <a href="{AUTHOR_URL}">Danila Katalshov</a> &middot; <a href="https://t.me/adanman">Telegram</a> &middot; <a href="https://www.linkedin.com/in/danilakatalshov">LinkedIn</a></p>
  <p><a href="{REPO_URL}">{SITE_NAME}</a> &middot; MIT</p>
</footer>
<script src="{p}assets/site.js"></script>
</body>
</html>"""


def load_editions() -> list[dict]:
    editions = []
    for idx in sorted(EDITIONS.glob("*/*/index.md")):
        meta, body = parse_md(idx)
        folder = idx.parent
        date = meta.get("date", f"{folder.parent.name}-{folder.name}")
        arts = []
        for f in sorted(folder.glob("[0-9][0-9]-*.md")):
            m, b = parse_md(f)
            ru, en = split_langs(b)
            m["_ru"], m["_en"] = ru, en
            m["_slug"] = f.stem
            arts.append(m)
        editions.append({"date": date, "num": meta.get("edition", "?"),
                         "cover": body, "articles": arts})
    editions.sort(key=lambda e: e["date"], reverse=True)
    return editions


def art_card(a: dict, href: str) -> str:
    rub = a.get("rubric", "tech")
    en_l, ru_l = RUBRICS.get(rub, RUBRICS["tech"])
    img = f'<img class="card-img" src="{html.escape(a["image"])}" alt="" loading="lazy">' if a.get("image") else ""
    return f"""<article class="card rubric-{rub}">
  {img}
  <span class="badge"><span class="lang-ru">{ru_l}</span><span class="lang-en">{en_l}</span></span>
  <h3><a href="{href}">
    <span class="lang-ru">{html.escape(a.get("title_ru", a["_slug"]))}</span>
    <span class="lang-en">{html.escape(a.get("title_en", a["_slug"]))}</span>
  </a></h3>
  <p class="dek"><span class="lang-ru">{html.escape(a.get("dek_ru", ""))}</span><span class="lang-en">{html.escape(a.get("dek_en", ""))}</span></p>
</article>"""


def edition_body(ed: dict, kicker_prefix_ru: str, kicker_prefix_en: str, href_prefix: str) -> str:
    cover_ru, cover_en = split_cover(ed["cover"])
    cards = "\n".join(art_card(a, f"{href_prefix}{a['_slug']}.html") for a in ed["articles"])
    return f"""<div class="edition-head">
  <p class="kicker"><span class="lang-ru">{kicker_prefix_ru} №{ed['num']}</span><span class="lang-en">{kicker_prefix_en} №{ed['num']}</span> &middot; {ed['date']}</p>
  <div class="editorial">
    <div class="lang-ru">{md_to_html(cover_ru)}</div>
    <div class="lang-en">{md_to_html(cover_en)}</div>
  </div>
</div>
<div class="grid">{cards}</div>"""


def render_article_page(a: dict) -> str:
    rub = a.get("rubric", "tech")
    en_l, ru_l = RUBRICS.get(rub, RUBRICS["tech"])
    img = f'<img class="hero-img" src="{html.escape(a["image"])}" alt="" loading="lazy">' if a.get("image") else ""
    src = html.escape(a.get("source", ""))
    return page(
        a.get("title_ru", a["_slug"]) + " - frontier-wire",
        f"""<article class="article">
  <p class="kicker"><span class="badge"><span class="lang-ru">{ru_l}</span><span class="lang-en">{en_l}</span></span> &middot; {a.get('date','')} &middot; <a href="index.html"><span class="lang-ru">весь выпуск</span><span class="lang-en">full edition</span></a></p>
  <h1><span class="lang-ru">{html.escape(a.get('title_ru',''))}</span><span class="lang-en">{html.escape(a.get('title_en',''))}</span></h1>
  <p class="dek big"><span class="lang-ru">{html.escape(a.get('dek_ru',''))}</span><span class="lang-en">{html.escape(a.get('dek_en',''))}</span></p>
  {img}
  <div class="prose lang-ru">{md_to_html(a['_ru'])}</div>
  <div class="prose lang-en">{md_to_html(a['_en'])}</div>
  <p class="srcline"><span class="lang-ru">Источник:</span><span class="lang-en">Source:</span> <a href="{src}">{src}</a></p>
</article>""",
        2,
        a.get("dek_en", ""),
    )


def main() -> int:
    editions = load_editions()

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)
    shutil.copytree(SRC / "assets", DOCS / "assets")

    for ed in editions:
        out = DOCS / "e" / ed["date"]
        out.mkdir(parents=True)
        (out / "index.html").write_text(
            page(f"frontier-wire - выпуск №{ed['num']} - {ed['date']}",
                 edition_body(ed, "Выпуск", "Edition", ""), 2), encoding="utf-8")
        for a in ed["articles"]:
            (out / f"{a['_slug']}.html").write_text(render_article_page(a), encoding="utf-8")

    if editions:
        latest = editions[0]
        front = edition_body(latest, "Свежий выпуск", "Latest edition", f"e/{latest['date']}/")
    else:
        front = "<p>Первый выпуск уже в печати. / First edition is at the press.</p>"
    (DOCS / "index.html").write_text(
        page("frontier-wire - все новости, дважды в день", front, 0), encoding="utf-8")

    rows = "\n".join(
        f'<li><a href="e/{e["date"]}/index.html">№{e["num"]} &middot; {e["date"]}</a>'
        f'<span class="count">{len(e["articles"])} <span class="lang-ru">материалов</span><span class="lang-en">stories</span></span></li>'
        for e in editions)
    (DOCS / "archive.html").write_text(
        page("frontier-wire - архив",
             f'<h1 class="page-title"><span class="lang-ru">Архив</span><span class="lang-en">Archive</span></h1><ul class="archive">{rows}</ul>', 0),
        encoding="utf-8")

    (DOCS / "404.html").write_text(
        page("404 - frontier-wire",
             '<div class="edition-head"><h1 class="page-title">404</h1><p class="lang-ru">Такой полосы нет. <a href="/frontier-wire/">На первую</a>.</p><p class="lang-en">No such page. <a href="/frontier-wire/">Front page</a>.</p></div>', 0),
        encoding="utf-8")

    n = sum(len(e["articles"]) for e in editions)
    print(f"Built docs/: {len(editions)} editions, {n} articles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
