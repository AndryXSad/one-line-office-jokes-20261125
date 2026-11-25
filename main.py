"""One-Line Office Jokes entry.

Writes one single-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke was picked by a local pairwise tournament over 12 original
candidates, judged against the bounty brief: a real office detail, the
laugh landing in the last few words, clear on one reading, fresh wording.
Winner (3-0, beat the fridge-lunch line in the final): the birthday card
that takes so long to travel the office its recipient has retired by the
time it arrives. The output is a fixed string, so every run is identical.
"""

import os

JOKE = (
    "We passed around a birthday card for Dave, and by the time it "
    "reached his desk he'd already retired."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = JOKE.strip()
    # The gate reads one line of 1-199 characters: enforce it here so a
    # bad edit fails loudly in our own run instead of at grading time.
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 199):
        raise SystemExit(f"entry is {len(text)} chars, gate needs 1-199")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
