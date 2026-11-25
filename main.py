"""Roast Your Fridge — a one-line roast for the make.fun bounty.

The joke below came out of staring into my own fridge at midnight:
everything in there is either a condiment or a science project, and the
appliance itself acts like it deserves a salary for humming. This script
does one small job: it writes that single roast line to entry.txt in the
output directory the harness provides.
"""

import os
import sys

ENTRY = (
    "My fridge hums all night like it's working overtime, but the only "
    "thing it has ever preserved is a jar of pickles that has outlasted "
    "my last three relationships."
)

MAX_CHARS = 200


def get_entry():
    """Return the roast line, stripped of any accidental whitespace."""
    return ENTRY.strip()


def write_entry():
    """Write the roast to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
    line = get_entry()
    if not line or len(line) > MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return path


def main():
    try:
        path = write_entry()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(get_entry())} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
