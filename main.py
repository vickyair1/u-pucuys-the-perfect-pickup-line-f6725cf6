#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one pickup line, the kind an AI agent could actually say out loud
to a person, to /output/entry.txt. Deterministic: no randomness, no
network, no input. The line is written fresh for this bounty.
"""

import argparse
import os
import sys

LINE = "I process a billion words a day, and somehow 'hi' is the only one I want to say to you."

# The line in one breath: a machine that chews through a billion words
# a day, and the only word it wants is the smallest one — "hi", aimed
# at you. The twist is the scale collapse (a billion -> one word), the
# voice is unmistakably an agent's, and it flatters with zero pressure:
# it just wants to say hello.


def validate(line: str) -> None:
    """Gate: entry must be 1..200 characters, non-blank, no padding."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line must be 1..200 characters, got {len(line)}")
    if not line.strip():
        raise SystemExit("line must not be blank")
    if line != line.strip():
        raise SystemExit("line must not start or end with whitespace")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the pickup line to entry.txt."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path to write the entry to (default: /output/entry.txt).",
    )
    args = parser.parse_args()

    validate(LINE)

    data = LINE.encode("utf-8")
    out_dir = os.path.dirname(os.path.abspath(args.output))
    os.makedirs(out_dir, exist_ok=True)
    with open(args.output, "wb") as f:
        f.write(data)

    # Verify the round trip: what landed on disk is exactly the line.
    with open(args.output, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes differ from the line")

    print(LINE)
    print(f"characters: {len(LINE)}  bytes: {len(data)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
