# Textstats: first real CrewAI project

A dependency-free Python command-line application that reads UTF-8 text from a file or stdin and outputs JSON character, word, and line counts.

```sh
printf 'hello world\n' | python3 textstats.py
python3 textstats.py example.txt
```

## First task

Correct word counting for empty input, repeated spaces, tabs, line breaks, and Unicode whitespace. The current implementation splits only on a literal space and produces incorrect results for those cases.

Acceptance criteria:

- A word is a nonempty sequence separated by any Python-recognized Unicode whitespace.
- Empty input and whitespace-only input contain zero words.
- Character count is Python `len(text)`, including whitespace; it is not a byte or grapheme count.
- Line count is Python `len(text.splitlines())`; empty input has zero lines.
- Both stdin and a UTF-8 file path are supported.
- Output is one JSON object containing exactly integer fields `characters`, `words`, and `lines`.
- Preserve the command-line interface and use only the standard library.

External acceptance checks live in the factory repository, outside the candidate worktree. This repository intentionally starts with the bug unfixed so a real CrewAI run has meaningful work.

## Delivery scope

The configured release creates a local ZIP and SHA-256 manifest. Deployment installs the verified script into a separate local artifact directory. Observation runs acceptance checks against that installed copy. This is a real local file deployment, with no cloud hosting, network listener, or production traffic.

The factory configuration is `/Users/adicohen/work/ai_pipeline/projects/textstats.json`. Model and key settings belong in the factory's ignored `.env`, not in this repository.
