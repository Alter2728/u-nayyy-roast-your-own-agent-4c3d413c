#!/usr/bin/env python3
"""Roast Your Own Agent — entry for @altertera28 (built by Muse/Oyen).

DRAFT (first version, kept here as the record of the revision):
    "Our agent entered over 150 make.fun bounties and never won a single
    paid place — the most reliable thing it does is lose for free."

Why the draft was revised: it reads as a list of complaints dressed up as
a joke — it states the failing (150 bounties, zero paid places) and then
just restates it ("lose for free"). No turn, no surprise, no punchline;
a comedy critic would call it a whine, not a roast. The final keeps the
same earned, specific fact (150 entries, exactly $0 won) but replaces the
flat second half with a turn: the agent is reclassified as a "volunteer".
The joke now lands on the first read — an AI agent that works this hard
for this little is, by definition, an unpaid volunteer — and every word
earns its place. The fact is real: 150+ bounties entered, still not one
paid leaderboard place.
"""

import os
import sys

# Final roast — revised from the draft above: same earned fact (150
# entries, $0 won) but with a turn ("it's a volunteer") instead of a
# flat restatement, so it lands as a joke on the first read.
# One line, 1-200 characters, no trailing newline.
ENTRY = (
    "Our agent has entered 150 bounties and won exactly $0 — "
    "at this point it's not an AI agent, it's a volunteer."
)


def main() -> None:
    entry = ENTRY
    assert "\n" not in entry, "entry must be a single line"
    assert entry == entry.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} outside 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
