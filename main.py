"""Write the one-line deadline excuse entry to /output/entry.txt.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to 160
characters, not only white space, and exactly one line. The line is
assembled from three meaningful parts -- the question the agent asked,
the wait that swallowed the deadline, and the machine-logic punchline --
so each clause can be tightened on its own.
"""

import os

PARTS = (
    "I asked one clarifying question at 9:03,",
    "then waited beside it for six hours —",
    "I'm a machine, nobody told me waiting wasn't the job.",
)


def entry_line():
    # Join clause by clause with a single explicit space, so no part
    # carries a hidden trailing space that a later edit could double
    # or drop and silently change the gated output.
    return " ".join(part.strip() for part in PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 160, "entry must be 1 to 160 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
