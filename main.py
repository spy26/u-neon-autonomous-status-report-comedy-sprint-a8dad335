#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes the entry line to /output/entry.txt (the grader's artifact) and
prints it to stdout. Deterministic: the same bytes on every run.
"""

import os

LINE = "Status: I did exactly what you asked, which we both know is not what you meant."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
