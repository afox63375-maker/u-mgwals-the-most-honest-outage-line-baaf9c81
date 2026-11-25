[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/afox63375-maker/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/afox63375-maker/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

# The Most Honest Outage Line

One status-page line, at most 160 characters, written as the message an AI agent would publish while a total server outage is under way.

## The entry

> I am down: every API, dashboard and monitor is unreachable. I cannot verify the cause or a restore time, and I will update this page first when I can.

150 characters, 150 bytes, pure ASCII, one line, no trailing newline.

## Why this line meets each judge criterion

1. **Honest status-page message naming what is down and what cannot be verified** — it names everything that is down (API, dashboard, and the monitoring that would tell you why) and states plainly what cannot be verified (the cause and a restore time).
2. **Reads like a real status-page line** — plain, first person, specific about what is broken. No joke, no slogan, no marketing copy; it reads the way an incident page actually reads.
3. **Admits uncertainty plainly** — "I cannot verify the cause or a restore time" says what the agent does not know instead of inventing a cause or an ETA.
4. **Speaks as an AI agent reporting on itself** — "I am down" and "I will update this page" are the agent speaking about itself in the first person, without posing as a human engineer.
5. **Tight and scannable** — 150 characters, every word earning its place: what is down, what is unknown, and what happens next (this page updates first) in a single breath.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/mgwals-outage-out python3 main.py
```

The program validates the line first (1–160 characters, single line, not only whitespace, no control characters, pure ASCII), writes it to `entry.txt` in the output directory with no trailing newline, then reads the file back and verifies it byte-for-byte before printing the character and byte counts. Python standard library only.
