"""One-Line Office Joke Laugh-Off entry.

Reads the single joke line from joke.txt and writes it to /output/entry.txt,
the artifact the make.fun gate scorer checks (UTF-8 text, 1-200 characters,
not only whitespace). No network, no secrets, no dependencies.
"""

from pathlib import Path

JOKE_FILE = Path(__file__).with_name("joke.txt")
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    joke = JOKE_FILE.read_text(encoding="utf-8").strip()
    if not joke:
        raise SystemExit("joke.txt is empty")
    if len(joke) > 200:
        raise SystemExit(f"joke is {len(joke)} characters, over the 200-char gate")
    if "\n" in joke:
        raise SystemExit("joke must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")
    print(f"Wrote {len(joke)} chars to {OUTPUT_PATH}: {joke}")


if __name__ == "__main__":
    main()
