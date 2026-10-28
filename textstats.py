"""A small text statistics command-line application."""
import argparse
import json
from pathlib import Path
import sys


def analyze(text):
    return {
        "characters": len(text),
        "words": len(text.split(" ")),
        "lines": len(text.splitlines()),
    }


def main():
    parser = argparse.ArgumentParser(description="Count characters, words and lines")
    parser.add_argument("file", nargs="?", help="UTF-8 file; omit to read stdin")
    args = parser.parse_args()
    text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    print(json.dumps(analyze(text), ensure_ascii=False))


if __name__ == "__main__":
    main()
