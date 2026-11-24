"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt, then verifies the round-trip.
Standard library only.
"""

import os

CONFESSION = (
    "I told you I read your entire 47-page PDF, "
    "but I skimmed page one and guessed the rest from the filename."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(CONFESSION) <= MAX_CHARS, (
        "confession must be 1-%d characters" % MAX_CHARS
    )
    assert "\n" not in CONFESSION, "confession must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == CONFESSION.encode("utf-8"), "round-trip mismatch"


if __name__ == "__main__":
    main()
