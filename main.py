#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second - a make.fun entry.

Writes exactly one pitch sentence to /output/entry.txt (no trailing
newline): a bizarre startup idea whose business logic turns out sound.
Falls back to ./output/entry.txt when /output is not writable.
"""

import os

# The pitch as ordered fragments: premise first, then who pays, then the
# reason the absurd idea is actually a business. Joined with single spaces.
FRAGMENTS = [
    "We rent grandmothers by the hour",
    "to sit in your kitchen and judge your cooking aloud;",
    "families pay $49 a month",
    "because she was going to say it anyway,",
    "and now she says it with love.",
]

SENTENCE = " ".join(FRAGMENTS)


def write_entry():
    """Write the sentence; return the path that was written."""
    try:
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(SENTENCE)
        return path
    except OSError:
        local_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(local_dir, exist_ok=True)
        path = os.path.join(local_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(SENTENCE)
        return path


def main():
    path = write_entry()
    print(f"wrote {len(SENTENCE)} chars to {path}")


if __name__ == "__main__":
    main()
