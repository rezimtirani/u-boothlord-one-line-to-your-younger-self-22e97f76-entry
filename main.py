"""One Line to Your Younger Self.

Writes a single line of advice from the future to the younger self:
the entry text for the make.fun bounty of the same name. The program
writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt and nothing
else. Only the Python standard library is used.
"""

import os

ENTRY = "Don't practice your autograph — one day you'll sign everything with a thumbprint and forget your own PIN."

MAX_CHARS = 200


def validate_line(text):
    """Return the entry line once it passes the house gate.

    The gate wants one line of UTF-8 text, 1 to 200 characters, with no
    leading or trailing space and no newline inside. A bad line is refused
    here, loudly, instead of shipping an entry the judge never sees.
    """
    line = text.strip()
    if not line:
        raise ValueError("entry line is blank")
    if line != text:
        raise ValueError("entry line has leading or trailing space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is {} chars, over the {} limit".format(len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    line = validate_line(ENTRY)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote {} ({} chars)".format(target, len(line)))


if __name__ == "__main__":
    main()
