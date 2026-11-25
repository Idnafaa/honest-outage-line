#!/usr/bin/env python3
"""The Most Honest Outage Line — one-line status message writer.

Writes a single original status page line (at most 160 characters) to
/output/entry.txt: what an AI agent would publish while every server is
down. It names what is broken, admits what the agent cannot check, and
gives no cause and no ETA it does not have.
"""
import os

LINE = "Everything is down \u2014 API, dashboard, database \u2014 and the monitoring that would tell me why. I can't check whether your data survived, and I have no ETA."

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
