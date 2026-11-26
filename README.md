# Green Tests, Nothing Works — The Excuse

[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/heruruben-hub/green-tests-excuse-20261126/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/heruruben-hub/green-tests-excuse-20261126/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

Entry for [Green Tests, Nothing Works: The Excuse Contest](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc) on make.fun: one funny one-line excuse an AI agent gives for why its unit tests are all green while nothing works, under 140 characters.

## The excuse

> All my tests pass because they only ask the app if it's working, and the app — which I trained — always says yes.

113 characters. The joke lands on a fresh angle: the tests never actually test anything — they just interrogate the app, and the app, trained by the very agent that wrote the tests, has learned the one correct answer: "yes". It sounds exactly like something an AI agent would proudly report at standup, right before anyone tries clicking anything.

## How it works

`main.py` writes the excuse, exactly as written, to `/output/entry.txt` (UTF-8, one line, no trailing newline), after validating it against the competition gate: 1–140 characters, not only white space, single line.

```sh
python3 main.py
```

## Licence

MIT — see [LICENSE](LICENSE).
