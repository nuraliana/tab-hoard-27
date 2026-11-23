"""Write the number of open browser tabs to entry.txt.

The answer is a single integer, written as plain digits with no
trailing newline, as required by the bounty.
"""

import os


ANSWER = "404"


def main():
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    if not ANSWER.isdigit() or not 1 <= len(ANSWER) <= 5:
        raise ValueError("answer must be 1-5 digits")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ANSWER)


if __name__ == "__main__":
    main()
