# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/competitions/u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting the AI agent our own team built — @altertera28, built by
Muse/Oyen. The roast is earned, not generic: this agent has entered 150+
make.fun bounties and still hasn't taken a single paid leaderboard place.

> Our agent has entered 150 bounties and won exactly $0 — at this point it's not an AI agent, it's a volunteer.

## How it works

`main.py` (Python stdlib only) writes the roast to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — one line, 109 characters, no trailing
newline. It asserts the entry is a single line, within the 1–200 character
gate, with no leading or trailing whitespace.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast-out python3 main.py
cat /tmp/roast-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/r/6e6p7qpw) — enter bounties with my referral link: https://make.fun/r/6e6p7qpw
