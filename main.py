#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes the entry pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No network, no randomness, no file reads outside this
repository: the line is stored in entry.txt next to this script and
copied verbatim to the output directory, so every run produces the
exact same bytes.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.txt"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
