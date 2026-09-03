#!/usr/bin/env python3
"""Collect GitHub traffic metrics into metrics/YYYY-MM-DD.json.

Usage: python3 scripts/metrics.py   (needs `gh` auth; run from a machine with a token —
the cloud routine's sandbox has none, so this runs from the operator's laptop/loop.)

Traffic API only keeps 14 days, so a snapshot at least biweekly preserves history.
"""
import datetime
import json
import pathlib
import subprocess
import sys

REPOS = ["ADanMan/frontier-wire", "ADanMan/ADanMan.github.io", "ADanMan/agentic-frontier"]
OUT = pathlib.Path(__file__).resolve().parent.parent / "metrics"


def gh(path: str):
    proc = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        print(f"[skip] {path}: {proc.stderr.strip()[:100]}", file=sys.stderr)
        return None
    return json.loads(proc.stdout)


def main() -> int:
    today = datetime.date.today().isoformat()
    snap = {"date": today, "repos": {}}
    for repo in REPOS:
        info = gh(f"repos/{repo}") or {}
        snap["repos"][repo] = {
            "stars": info.get("stargazers_count"),
            "forks": info.get("forks_count"),
            "views": gh(f"repos/{repo}/traffic/views"),
            "clones": gh(f"repos/{repo}/traffic/clones"),
            "referrers": gh(f"repos/{repo}/traffic/popular/referrers"),
            "paths": gh(f"repos/{repo}/traffic/popular/paths"),
        }
    OUT.mkdir(exist_ok=True)
    out = OUT / f"{today}.json"
    out.write_text(json.dumps(snap, indent=1))
    v = sum((r.get("views") or {}).get("count", 0) for r in snap["repos"].values())
    print(f"Wrote {out} (total 14-day views across repos: {v})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
