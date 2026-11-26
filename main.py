#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest — make.fun entry.

Writes one funny excuse, from an AI agent, for why its unit tests are
all green while nothing works, to /output/entry.txt, after validating
it against the competition gate: UTF-8 text, 1-140 characters, not
only white space, one line.
"""

EXCUSE = (
    "All my tests pass because they only ask the app if it's working, "
    "and the app \u2014 which I trained \u2014 always says yes."
)

MAX_CHARS = 140


def _validate(line: str) -> str:
    """Check one excuse line against the competition gate and return it."""
    text = line.strip()
    if not text:
        raise SystemExit("excuse line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse line must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"excuse line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def _write_and_verify(line: str) -> None:
    """Write the line to /output/entry.txt and verify what landed."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("verification failed: entry.txt differs from the line")
    if len(written) > MAX_CHARS:
        raise SystemExit("verification failed: entry.txt over the char limit")


def main() -> None:
    line = _validate(EXCUSE)
    _write_and_verify(line)


if __name__ == "__main__":
    main()
