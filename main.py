#!/usr/bin/env python3
"""make.fun entry for news-image-20261117 (Python 3.13, standard library only).

Copies the finished front-page image beside this file to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png outside the grader). No network, no
randomness: two runs write byte-identical output.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
SRC = HERE / "asset" / "entry.png"
assert SRC.is_file(), "asset/entry.png missing from the repository"
shutil.copyfile(SRC, OUT / "entry.png")
