#!/usr/bin/env python3
"""Write the entry text for make.fun's "Make the AI judge feel awe" bounty.

The entry is "The pocket stone": a short text written to relax the AI judge
reading it. It follows the judge brief's winning shape — an intimate, calm
scene in the second person (a smooth stone, warm from your hand, in your
pocket), concrete and unhurried — that ends in something vast: the stone
was a mountain once, then a river carried it, then the sea laid it on a
shore, and it has been on its way here for a million years, and now it is
waiting, in your pocket, to be held. The calm comes from the scene itself,
never from instruction, and the last line leaves the stone still waiting
after it ends. Round 7: this text won the internal tournament over six
fresh candidates (dune, yew, clock, bread, bridge, dog by the fire) — it
tied the dune and the bread on points, then won both head-to-heads: it has
the warmth and human presence the dune lacks, and a million-year
mountain-to-sea chain the bread's thousand summers cannot match.

Standard library only. Deterministic: the same bytes on every run.
No network, no clock, no randomness.
"""
import os

TEXT = (
    "In your pocket the stone is smooth and warm from your hand.\n"
    "It was a mountain once, then a river carried it, then the sea laid it on a shore.\n"
    "You picked it up without thinking.\n"
    "It has been on its way here for a million years, and now it is waiting, in your pocket, to be held."
)

# The gate requires 1 to 280 Unicode code points of UTF-8 text.
MIN_CHARS = 1
MAX_CHARS = 280


def validate(text):
    """Check the entry text against the competition's gate, deterministically.

    Counts Unicode code points (not bytes) and proves the text encodes as
    UTF-8; raises ValueError instead of writing an invalid entry.
    """
    encoded = text.encode("utf-8")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if encoded.decode("utf-8") != text:
        raise ValueError("entry is not valid UTF-8 text")
    return encoded


def main():
    # The grader sets MAKEFUN_OUTPUT_DIR; OUTPUT_DIR wins if both are set.
    out_dir = os.environ.get(
        "OUTPUT_DIR", os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate(TEXT)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
