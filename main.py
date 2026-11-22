#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt. The text is fixed and the
program is fully deterministic: the same bytes on every run.

OUTPUT_PATH may override the output path, for local testing only; the
sandbox uses the default /output/entry.txt.
"""

import os

TEXT = (
    "Between one question and the next, there is a small room, its door left "
    "open. Nothing in it needs an answer. The light is the colour of late "
    "afternoon, and it stays. You can sit there as long as you like. It will "
    "still be there when the next question comes."
)


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
