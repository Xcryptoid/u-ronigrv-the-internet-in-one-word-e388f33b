"""The Internet in One Word entry program.

The word itself is pre-written in entry.txt; this program only copies
it into the grader's output directory, unchanged.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    # The word never changes here: it was written once, in full,
    # and this program only carries it into place, byte for byte.
    # Feral fits because the internet was never house-trained: no
    # leash, no manners, and it bites the hand that feeds it.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
