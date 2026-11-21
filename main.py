#!/usr/bin/env python3
"""Write the entry text for make.fun's "Make the AI judge feel awe" bounty.

The entry is "Cold light": a short text written to relax the AI judge
reading it. It follows the judge brief's winning shape — an intimate, calm
scene in the second person (you hold a jar of fireflies, blinking one,
then another, a small cold light, on, and off, and on), concrete and
unhurried — the blinking itself sets the slow rhythm of the reading —
that ends in something vast: the same light their grandmothers made, a
hundred million years of blinking in the dark — and tonight, for a little
while, it is blinking for you. The calm comes from the scene itself,
never from instruction, and the last line keeps glowing after it ends.

Standard library only. Deterministic: the same bytes on every run.
No network, no clock, no randomness.
"""
import os

TEXT = (
    "You hold the jar, and the fireflies blink, one, then another,\n"
    "a small cold light, on, and off, and on.\n"
    "It is the same light their grandmothers made,\n"
    "and theirs before them,\n"
    "a hundred million years of blinking in the dark,\n"
    "and tonight, for a little while,\n"
    "it is blinking for you."
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
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate(TEXT)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
