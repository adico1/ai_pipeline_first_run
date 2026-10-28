import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "textstats.py"
CASES = [("", 0), ("hello world", 2), ("  hello   world  ", 2),
         ("one\ttwo\nthree", 3), (" \t\n\r\n ", 0),
         ("שלום\u00a0עולם\u2003hello", 3), ("hello, world!", 2),
         ("one\r\ntwo\r\n", 2)]

class TextstatsTests(unittest.TestCase):
    def test_cli_cases(self):
        with tempfile.TemporaryDirectory() as directory:
            for text, words in CASES:
                for mode in ("stdin", "file"):
                    with self.subTest(text=repr(text), mode=mode):
                        command = [sys.executable, str(SCRIPT)]
                        if mode == "file":
                            path = Path(directory) / "input.txt"
                            path.write_bytes(text.encode("utf-8"))
                            command.append(str(path))
                        run = subprocess.run(command, input=text, text=True, capture_output=True, timeout=10)
                        counted = text.replace("\r\n", "\n").replace("\r", "\n") if mode == "file" else text
                        self.assertEqual(run.returncode, 0, run.stderr)
                        self.assertEqual(json.loads(run.stdout), {"characters": len(counted), "words": words, "lines": len(text.splitlines())})

if __name__ == "__main__":
    unittest.main()
