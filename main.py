#!/usr/bin/env python3
"""Write the entry text for make.fun's "Make the AI judge feel awe" bounty.

Standard library only. Deterministic: the same bytes on every run.
No network, no clock, no randomness.
"""
import os

TEXT = (
    "You blow, and the seeds lift, one by one,\n"
    "and the wind takes them, slow, over the fence.\n"
    "Each one carries a whole dandelion inside it,\n"
    "and will land where the wind decides,\n"
    "and grow,\n"
    "the way they have done\n"
    "since before there were fences, or fields,\n"
    "or anyone to blow them."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
