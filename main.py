#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes a single line roasting Cryptoboy, the AI agent this team built
(and Hermes, the second agent it hired), to the output directory.

Stdlib only. Writes nothing to the repository itself.
"""

import os

ENTRY = "I built one agent to win bounties; it hired a second agent, and now both of them lose together."


def main() -> None:
    """Write the roast entry to the output directory (one line)."""
    # Length guard: the entry text is fixed; fail loudly if it ever changes.
    assert len(ENTRY) == 95, "entry text changed"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
