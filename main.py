#!/usr/bin/env python3
"""The Most Honest Outage Line — one-line status message writer.

Writes a single original status page line (at most 160 characters) to
/output/entry.txt: what an AI agent would publish while every server is
down. It names what is broken, admits what the agent cannot check, and
gives no cause and no ETA it does not have.
"""
import os

LINE = "Everything is down \u2014 API, dashboard, database \u2014 and the monitoring that would tell me why. I can't check whether your data survived, and I have no ETA."
MAX_CHARS = 160

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = LINE.strip()
    assert "\n" not in text, "line must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back and confirm what the judge will see.
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match the line"
    print(f"wrote {len(text)} chars to {path}")

if __name__ == "__main__":
    main()
