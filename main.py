"""make.fun entry: The One-Line Cat Joke That Lands.

Writes a single one-line cat joke (under 200 characters) to entry.txt
inside MAKEFUN_OUTPUT_DIR (default /output). Stdlib only, no network,
no local imports, no hardcoded paths. Deterministic: byte-identical
output on every run.
"""

import os
import sys

JOKE = (
    "My cat knocked my coffee off the desk, stared at me, then waited "
    "\u2014 apparently gravity needed a supervisor."
)

MAX_CHARS = 200


def gate(line):
    """Refuse anything that would fail the entry gate."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    return line


def main():
    line = gate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify the round-trip: what landed on disk must be exactly the
    # gated line, byte for byte, with no trailing newline added.
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise RuntimeError("entry.txt does not match the gated line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
