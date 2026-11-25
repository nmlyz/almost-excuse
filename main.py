"""Write the excuse line to /output/entry.txt.

The program writes exactly one line of plain text, no trailing newline.
"""

from pathlib import Path

ENTRY = "My badge stopped working after Friday's reissue and security won't let me past the lobby."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
