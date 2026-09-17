#!/usr/bin/env python3
"""Backfill historical weeks by driving monitor.py once per historical run-date.

Each week gets its own monitor run whose window ends on that week's Sunday, so
papers land in their own publication week on the site (the same week key the
weekly cron produces) and no single fetch runs into PubMed's retmax=500 or
arXiv's max_results cap — a multi-year window would silently blow past both.

    python scripts/backfill.py --since 2025-09-15 --until 2026-09-14 --dry-run
    python scripts/backfill.py --since 2025-09-15 --until 2026-09-14
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MONITOR = os.path.join(HERE, "monitor.py")
WINDOW_DAYS = 7
REQUIRED_ENV = ("ENTREZ_EMAIL", "LLM_API_KEY")


def monday_run_dates(since: str, until: str) -> list[str]:
    """Every Monday in [since, until] as ISO dates.

    A Monday run-date D yields the window [D-7, D-1] — one calendar week ending
    on the preceding Sunday.
    """
    start = dt.date.fromisoformat(since)
    end = dt.date.fromisoformat(until)
    if end < start:
        return []
    day = start + dt.timedelta(days=(-start.weekday()) % 7)
    out = []
    while day <= end:
        out.append(day.isoformat())
        day += dt.timedelta(days=7)
    return out


def week_args(run_date: str, config: str, out_dir: str) -> list[str]:
    return [
        "--config", config,
        "--out-dir", out_dir,
        "--run-date", run_date,
        "--window-days", str(WINDOW_DAYS),
    ]


def missing_env() -> list[str]:
    return [name for name in REQUIRED_ENV if not (os.environ.get(name) or "").strip()]


def parse_args():
    p = argparse.ArgumentParser(description="Backfill historical weeks via monitor.py.")
    p.add_argument("--since", required=True, help="Earliest run-date (YYYY-MM-DD); snapped forward to a Monday")
    p.add_argument("--until", required=True, help="Latest run-date (YYYY-MM-DD); snapped back to a Monday")
    p.add_argument("--config", default="config.yaml")
    p.add_argument("--out-dir", default=".")
    p.add_argument("--dry-run", action="store_true", help="Print the week plan and exit")
    return p.parse_args()


def _window(run_date: str) -> str:
    d = dt.date.fromisoformat(run_date)
    return f"{(d - dt.timedelta(days=WINDOW_DAYS)).isoformat()} .. {(d - dt.timedelta(days=1)).isoformat()}"


def main():
    args = parse_args()
    weeks = monday_run_dates(args.since, args.until)
    if not weeks:
        print(f"No Monday in {args.since} .. {args.until}; nothing to do.", file=sys.stderr)
        return 1

    first = dt.date.fromisoformat(weeks[0]) - dt.timedelta(days=WINDOW_DAYS)
    last = dt.date.fromisoformat(weeks[-1]) - dt.timedelta(days=1)
    print(f"{len(weeks)} week(s), covering {first} .. {last}")
    if args.dry_run:
        for w in weeks:
            print(f"  run-date {w}  ->  window {_window(w)}")
        return 0

    missing = missing_env()
    if missing:
        print(f"Missing env var(s): {', '.join(missing)}. Refusing to start.", file=sys.stderr)
        return 1

    failed = []
    for i, week in enumerate(weeks, 1):
        print(f"[{i}/{len(weeks)}] run-date {week}  window {_window(week)}", flush=True)
        rc = subprocess.call([sys.executable, MONITOR] + week_args(week, args.config, args.out_dir))
        if rc != 0:
            failed.append(week)
            print(f"[{i}/{len(weeks)}] {week} FAILED (exit {rc})", file=sys.stderr, flush=True)

    if failed:
        print(f"\n{len(failed)} of {len(weeks)} week(s) failed: {', '.join(failed)}", file=sys.stderr)
        print(f"Retry: {sys.argv[0]} --since {failed[0]} --until {failed[-1]}", file=sys.stderr)
        return 1
    print(f"\nAll {len(weeks)} week(s) done. Now run: python scripts/build_site.py --out-dir . --config config.yaml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
