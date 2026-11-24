#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes the entry line to /output/entry.txt (the grader's artifact) and
prints it to stdout. Deterministic: the same bytes on every run.
"""

import os

LINE = "Status: I did exactly what you asked, which we both know is not what you meant."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(f"entry line is {len(LINE)} chars, outside 1..{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
