#!/usr/bin/env bash
# Open-network digest bridge.
# The cloud routine's sandbox reaches only raw.githubusercontent.com, so every
# non-mirror feed in feeds.txt is invisible to it. This script runs on the
# operator's Mac (open network), builds the full digest and pushes it; the
# routine then reuses the ready file instead of refetching a narrow one.
# Runs on the operator's Mac (launchd, ~/Library/LaunchAgents/com.frontierwire.digest.plist)
# and on the Hostkey VPS (systemd timer frontier-wire-digest.timer, clone in /opt/frontier-wire).
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"  # repo = parent of scripts/, wherever this clone lives
export PATH="/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin"
cd "$REPO"
git pull --rebase --autostash -q origin main
python3 scripts/digest.py
if [ -n "$(git status --porcelain digests/)" ]; then  # new files are untracked, git diff misses them
  git add digests/
  git commit -q -m "digest: $(date -u +%Y-%m-%d) (open-network)" \
    --author="Danila Katalshov <56929384+ADanMan@users.noreply.github.com>"
  git push -q origin main
  echo "$(date -u) pushed digest"
else
  echo "$(date -u) digest unchanged"
fi
