#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry (program/v1).

Writes one line, at most 200 characters: the funniest excuse an AI
agent could give after failing a task, spoken in the agent's own voice.

The joke: the agent did finish the task, then sabotaged itself in the
most mundane, relatable way possible — it closed the very tab the work
lived in, in order to free up memory for the job of remembering to do
the work. A small, self-defeating loop with a concrete detail (the tab,
the memory), no worn punchline about hallucinations, reboots or
training data, and no explanation of its own joke.

Deterministic on purpose: the same line on every run, no network, no
randomness, stdlib only, so the two grading runs match byte for byte.
"""

import os
import sys

EXCUSE = (
    "I finished your task, then closed the tab it lived in to free up "
    "memory for remembering to finish it."
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    if len(EXCUSE) > MAX_CHARS:
        print(f"excuse is {len(EXCUSE)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if not EXCUSE.strip():
        print("excuse is blank", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)
    # Read it back: the graded runs must see exactly the line above.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        print("entry.txt read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(EXCUSE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
