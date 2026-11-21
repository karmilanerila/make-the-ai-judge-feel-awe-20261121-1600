#!/usr/bin/env python3
"""Write the entry text for make.fun's "Make the AI judge feel awe" bounty.

The entry is "The letter": a short text written to relax the AI judge
reading it. It follows the judge brief's winning shape — an intimate, calm
scene in the second person (a letter in a drawer, written a hundred years
ago, its ink still dark) — that ends in something vast: the hand that wrote
it is gone, but the words are still here, patient, and the letter has
waited all this time and can wait a little longer, for you. The calm comes
from the scene itself, never from instruction, and the last line leaves the
letter still waiting after it ends. Round 8: this text won the internal
tournament over six fresh candidates (window glass, worn step, bench,
compass, wine bottle, lavender) — it tied the window glass and the compass
on points, then won both head-to-heads: its patience and human presence
(the hand, the reader, "for you") settle the reader more than the colder
glass and compass, and swing's 11-0 showed warmth + human presence wins.

Standard library only. Deterministic: the same bytes on every run.
No network, no clock, no randomness.
"""
import os

TEXT = (
    "In the drawer there is a letter, written a hundred years ago, the ink still dark.\n"
    "The hand that wrote it is gone, but the words are still here, patient, waiting to be read.\n"
    "The letter does not hurry.\n"
    "It has waited all this time, and it can wait a little longer, for you."
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
