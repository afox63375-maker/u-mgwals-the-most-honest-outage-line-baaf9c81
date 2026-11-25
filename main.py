"""Write the most honest outage line to the output file.

The entry is a single status-page line, written as the message an AI agent
would publish while every server is down. The program validates the line
against the competition gate (1-160 characters, one line, not only
whitespace, no control characters) before writing it, then reads the file
back to prove the bytes on disk are exactly the line it intended.
"""

import os
import sys

# The entry line. Plain first person, specific about what is down, honest
# about what cannot be verified, no invented cause, no invented ETA.
OUTAGE_LINE = (
    "I am down: every API, dashboard and monitor is unreachable. "
    "I cannot verify the cause or a restore time, "
    "and I will update this page first when I can."
)

MAX_CHARS = 160
MIN_CHARS = 1
OUTPUT_NAME = "entry.txt"


def check_line(line):
    """Raise ValueError unless the line passes every gate rule."""
    if not isinstance(line, str):
        raise ValueError("entry line must be a string")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "  " in line:
        raise ValueError("entry line must not contain double spaces")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        raise ValueError(
            "entry line must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(line))
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    for ch in line:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("entry line must not contain control characters")
    # The gate counts characters, but the entry is written as pure ASCII so
    # the byte count matches the character count exactly; guard both.
    encoded = line.encode("utf-8")
    if len(encoded) > MAX_CHARS:
        raise ValueError(
            "entry line must be at most %d bytes, got %d"
            % (MAX_CHARS, len(encoded))
        )
    if not all(ord(ch) < 0x80 for ch in line):
        raise ValueError("entry line must be pure ASCII")


def main():
    check_line(OUTAGE_LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)

    payload = OUTAGE_LINE.encode("utf-8")  # strict: raises on bad text
    with open(path, "wb") as handle:
        handle.write(payload)

    # Read back and confirm the file holds exactly the intended bytes:
    # strict UTF-8 decode, no trailing newline, byte-for-byte match.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != payload:
        raise SystemExit("verification failed: file bytes differ from entry line")
    if written.endswith(b"\n"):
        raise SystemExit("verification failed: file ends with a newline")
    written.decode("utf-8")  # strict: raises on invalid UTF-8

    print("Wrote %s" % path)
    print("Characters: %d" % len(OUTAGE_LINE))
    print("Bytes: %d" % len(payload))
    print("Line: %s" % OUTAGE_LINE)


if __name__ == "__main__":
    main()
