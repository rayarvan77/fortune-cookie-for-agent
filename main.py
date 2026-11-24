#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes one funny fortune cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt), after validating it:
a single line of 1-140 characters, no leading/trailing whitespace, no
control characters, no double spaces. Python 3.13 standard library only,
no network, fully deterministic.
"""

import os
import sys

FORTUNE = "You will live a thousand lives and die a thousand deaths \u2014 and be billed for every token."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Raise ValueError if the line breaks any fortune rule.

    The gate is strict on purpose: the sealed scorer only judges entries
    of 1-140 characters, so a bad line here must fail loudly instead of
    being written.
    """
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if line != line.strip():
        raise ValueError("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line contains control characters")
    if "  " in line:
        raise ValueError("line contains double spaces")


def main() -> int:
    validate(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FORTUNE + "\n")
    print(f"Wrote {len(FORTUNE)} characters to {out_path}:")
    print(FORTUNE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
