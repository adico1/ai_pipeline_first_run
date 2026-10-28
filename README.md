# Textstats

A dependency-free Python CLI that reports character, word, and line counts as JSON. Requires Python 3.11 or later.

## Run

```sh
printf 'hello   world\n' | python3 textstats.py
python3 textstats.py path/to/input.txt
```

Output for the first example:

```json
{"characters": 14, "words": 2, "lines": 1}
```

Words are separated by Python-recognized Unicode whitespace. Empty or whitespace-only text contains zero words. Characters use `len(text)`; lines use `len(text.splitlines())`. Reading a UTF-8 file normalizes CRLF line endings through Python text I/O before character counting. The CLI accepts stdin or one UTF-8 file path and uses only the standard library.

## Test

```sh
python3 -m unittest discover -s tests -v
```

The suite covers 16 stdin/file scenarios, including Unicode, tabs, repeated spaces, empty input, punctuation, and line endings. GitHub Actions runs it on Python 3.11 and 3.13.

## Release v0.1.0

Fixes incorrect word counts caused by splitting only on a literal space. The corrected source completed the CrewAI software-factory workflow, external acceptance checks, a limited static import policy check, and checks against a locally installed release. The repository tests can be run independently of the factory. No web service or cloud runtime is required.
