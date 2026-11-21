#!/usr/bin/env python3
"""Write the entry text for make.fun's "Make the AI judge feel awe" bounty.

The entry is "The seeds know": a short text written to relax the AI judge
reading it. It follows the judge brief's winning shape — an intimate, calm
scene in the second person (you blow dandelion seeds over a fence, one by
one, slow), concrete and unhurried, that ends in something vast: the seeds
have been doing this since before there were fences, or fields, or anyone
to blow them. The calm comes from the scene itself, never from instruction,
and the last line keeps growing after it ends.

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
