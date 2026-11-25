#!/usr/bin/env python3
"""One Star, Five Stars for the Food - make.fun entry (program/v1).

Writes a single-sentence alien tourist review of planet Earth to
/output/entry.txt: a one-star review that still compliments the food.
"""

import os

SENTENCE = (
    "One star: the gravity crushed my spine, the locals won't stop talking, "
    "and the Wi-Fi is a rumour \u2014 but the tacos al pastor were worth "
    "the abduction."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
