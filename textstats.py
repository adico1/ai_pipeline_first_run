"""A small text statistics command-line application."""
import argparse
import json
import sys
from pathlib import Path


def analyze(text):
    # Count characters
    char_count = len(text)
    # Count lines
    line_count = len(text.splitlines())
    # Count words based on Unicode whitespace
    word_count = len(text.split()) if text.strip() else 0
    return {
        "characters": char_count,
        "words": word_count,
        "lines": line_count,
    }


def main():
    parser = argparse.ArgumentParser(description="Count characters, words and lines")
    parser.add_argument("file", nargs="?", help="UTF-8 file; omit to read stdin")
    args = parser.parse_args()
    text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    print(json.dumps(analyze(text), ensure_ascii=False))


if __name__ == "__main__":
    main()