#!/usr/bin/env python3
"""make.fun bounty entry: Sum up 24 November's world news in one image.

The entry image is bundled in this repository as front-page.png.
This program copies it, byte for byte, to /output/entry.png.

No network access, no randomness, no dependencies beyond the standard
library: running it twice writes identical bytes, as the rules require.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "front-page.png")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print("wrote", OUTPUT, os.path.getsize(OUTPUT), "bytes")


if __name__ == "__main__":
    sys.exit(main())
