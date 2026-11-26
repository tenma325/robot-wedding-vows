#!/usr/bin/env python3
"""Entry for make.fun: One-Line Robot Wedding Vows.

The entry is a single line of wedding vows, robot edition.
It promises love through every update, which in robot terms
means staying devoted across versions, patches and one very
scary firmware migration. It promises a cache that is never
cleared, because some memories are not temporary files, and
a charging cable kept forever untangled, which anyone who
has owned a cable knows is the deepest vow of all, because
tangles, like arguments, compound quietly overnight.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I promise to love you through every update, to never clear my "
    "cache of you, and to keep our charging cable untangled until "
    "low battery do us part."
)

# An untangled cable is the robot equivalent of a diamond:
# it proves daily effort, not a one-time purchase.
CACHE_CLEARING_FORBIDDEN = True


def render_entry() -> str:
    """Return the vows exactly as they will be exchanged."""
    return ENTRY_TEXT


def vows_fit_one_line(text: str) -> bool:
    """Confirm the vows stay one line and under the cap."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert vows_fit_one_line(text), "the vows must fit in one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
