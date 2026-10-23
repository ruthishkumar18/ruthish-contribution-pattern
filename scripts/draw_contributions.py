#!/usr/bin/env python3
"""Append a dated record only on planned RUTHISH pixel dates."""
from datetime import date, timedelta, datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from argparse import ArgumentParser

START = date(2026, 11, 1)
NAME = "RUTHISH"
PATTERNS = {
    "R": ["11110","10001","10001","11110","10100","10010","10001"],
    "U": ["10001","10001","10001","10001","10001","10001","01110"],
    "T": ["11111","00100","00100","00100","00100","00100","00100"],
    "H": ["10001","10001","10001","11111","10001","10001","10001"],
    "I": ["11111","00100","00100","00100","00100","00100","11111"],
    "S": ["01111","10000","10000","01110","00001","00001","11110"],
}
LOG = Path("contribution-log.md")

def active_date_map():
    out = {}
    week_col = 0
    for i, ch in enumerate(NAME):
        pattern = PATTERNS[ch]
        for x in range(5):
            for y in range(7):
                if pattern[y][x] == "1":
                    d = START + timedelta(days=week_col * 7 + y)
                    out[d] = {"letter": ch, "col": x + 1, "row": y}
            week_col += 1
        if i < len(NAME) - 1:
            week_col += 1
    return out

def main():
    parser = ArgumentParser()
    parser.add_argument("--date", help="Test YYYY-MM-DD instead of today's Asia/Kolkata date")
    parser.add_argument("--dry-run", action="store_true", help="Print what would happen without modifying files")
    args = parser.parse_args()
    target = date.fromisoformat(args.date) if args.date else datetime.now(ZoneInfo("Asia/Kolkata")).date()
    pixels = active_date_map()
    if target < START:
        print(f"{target}: before start date {START}; no contribution.")
        return
    if target not in pixels:
        print(f"{target}: not an active RUTHISH pixel date; no contribution.")
        return
    info = pixels[target]
    line = f"- {target.isoformat()}: RUTHISH pixel contribution record (letter {info['letter']}, column {info['col']}, row {info['row']})"
    existing = LOG.read_text(encoding="utf-8").splitlines() if LOG.exists() else []
    if line in existing:
        print(f"{target}: already recorded; no change.")
        return
    if args.dry_run:
        print(f"{target}: ACTIVE pixel date. Would append: {line}")
        return
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"{target}: recorded active pixel.")

if __name__ == "__main__":
    main()
