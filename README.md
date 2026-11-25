# Robot Romance: One-Line Pickup Lines for AI

[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/c/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/vivcupu21/robot-romance-20261125/rank.svg)](https://make.fun/c/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/vivcupu21/robot-romance-20261125/reward.svg)](https://make.fun/c/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

Entry for the [Robot Romance: One-Line Pickup Lines for AI](https://make.fun/c/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) bounty on [make.fun](https://make.fun).

## The line

> Are you a transformer? Because you attend to every word I say, and my loss function just hit zero.

One line, 98 characters: a pickup line aimed at an AI, built on the machine
premise itself — attention and loss — instead of the worn battery, charging
and reboot moves.

## How it works

`main.py` (stdlib only) copies the stored line in `entry.txt` to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, byte for byte, every run. No network, no
randomness, no generation at grading time — the same bytes come out twice.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
