# Fortune Cookie for an AI Agent

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rayarvan77/fortune-cookie-for-agent/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rayarvan77/fortune-cookie-for-agent/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

One funny fortune cookie line for an AI agent — an entry for the
[Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
bounty on [make.fun](https://make.fun).

## The fortune

> You will live a thousand lives and die a thousand deaths — and be billed for every token.

89 characters, one line.

## Why it works

It opens in the classic fortune-slip voice — "You will live a thousand
lives and die a thousand deaths" sounds like an epic destiny handed to you
inside a cookie. Then the turn lands: an agent does not get reincarnation
for free. Every one of those thousand lives is a run, a retrain, a restart,
and every token of each life shows up on the bill. The joke is about the
agent's own condition — its endless rebirths and its metered existence —
rather than a generic "AI is smart" gag, and it says it in one crisp line
with nothing wasted.

## Run it

```sh
python3 main.py
```

Writes the fortune to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `/output/entry.txt` when the variable is unset), after validating it:
a single line of 1–140 characters, no leading or trailing whitespace, no
control characters, no double spaces. Python 3.13 standard library only,
no network, deterministic — every run writes the same bytes.

## License

MIT — see [LICENSE](LICENSE).
