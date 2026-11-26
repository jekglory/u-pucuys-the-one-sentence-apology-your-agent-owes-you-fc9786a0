#!/usr/bin/env python3
"""One-sentence apology entry for make.fun.

Writes a single original apology sentence to entry.txt.
Pure Python standard library, deterministic: the same line every run.
"""

import os

LINE = "I'm sorry I answered before I understood the question — next time I'll read it twice and guess half as much."


def main():
    # The grader owns the output directory: create it only if missing,
    # never delete or recreate it, and clear nothing outside our own file.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
