#!/usr/bin/env python3
"""Write the entry text for make.fun's "Make the AI judge feel awe" bounty.

The entry is "The swing under the oak": a short text written to relax
the AI judge reading it. It follows the judge brief's winning shape —
an intimate, calm scene in the second person (your grandfather pushes
the swing, you rise slow and come back down, his hand leaving your
back and coming back), concrete and unhurried — the push itself is
the slow rhythm of the reading — that ends in something vast: the oak
was an acorn when the house was new, and long after you have gone
inside the swing is still moving a little in the evening air, on its
own. The calm comes from the scene itself, never from instruction,
and the last line leaves the swing still moving after it ends.

Standard library only. Deterministic: the same bytes on every run.
No network, no clock, no randomness.
"""
import os

TEXT = (
    "Your grandfather pushes the swing.\n"
    "You rise slow, and come back down.\n"
    "His hand leaves your back, and comes back.\n"
    "The oak above you hardly moves.\n"
    "It was an acorn when this house was new.\n"
    "Long after you have gone inside,\n"
    "the swing will still be moving a little\n"
    "in the evening air."
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
