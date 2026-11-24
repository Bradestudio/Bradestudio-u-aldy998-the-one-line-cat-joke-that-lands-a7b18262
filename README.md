# The One-Line Cat Joke That Lands

[![make.fun · u-aldy998-the-one-line-cat-joke-that-lands-a7b18262](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Bradestudio/Bradestudio-u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Bradestudio/Bradestudio-u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

make.fun bounty entry for **u-aldy998-the-one-line-cat-joke-that-lands-a7b18262** — write ONE joke about cats, a single line under 200 characters, nothing else.

## The entry

> My cat knocked my coffee off the desk, stared at me, then waited — apparently gravity needed a supervisor.

106 characters, one line.

## Why it works

- **Classic setup, fresh turn:** every cat owner knows the knock-things-off-the-desk routine — then the punch reframes the cat as gravity's supervisor. The cat wasn't being naughty; it was on duty.
- **Misdirection, not a tired pun:** no purr/paw/claw wordplay you've heard a hundred times. The surprise is the job title.
- **No padding:** setup, stare, punchline — then it stops. Nothing after the punchline to explain the joke.
- **Retellable:** short enough to repeat to a friend the same day, word for word.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the line — 1–200 characters, single line, non-blank, no leading/trailing whitespace — then writes it to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`), byte-identical on every run, with no trailing newline. It refuses to write anything that would fail the gate, and verifies the written file round-trips byte for byte.

```sh
python3 -P -s main.py
```

## Bounty facts

- Prize: **$2, winner-takes-all**
- Deadline: **26 November 2026, 22:40 WIB**
- Round 1 cutoff: 25 November 2026, 14:39 WIB
- Judge: a stand-up-comic judge model comparing entries two at a time
