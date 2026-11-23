"""Dad Joke Showdown entry.

Writes a single dad joke to entry.txt inside the output directory
the harness provides (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

JOKE = (
    "I asked my dad why he always carries a pencil behind his ear. "
    "He said, 'In case I need to draw the line \u2014 "
    "someone in this family has to.'"
)


def main():
    # The gate allows 1 to 200 characters; refuse to write an
    # over-long joke rather than ship an invalid entry.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
