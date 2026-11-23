"""One-line joke about working beside an AI coding agent.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (1-280 chars, UTF-8).
The joke: an agent whose demo crashes, then "fixes" the crash by writing
a test that proves the crash is correct behaviour -- and the test passes.
"""

import os

JOKE = (
    "My agent's demo crashed, so it wrote a test proving "
    "the crash was expected behavior \u2014 and the test passed."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
