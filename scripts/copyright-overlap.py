#!/usr/bin/env python3
"""Flag word sequences in the book that also appear in the E-Myth source material.

Usage: python3 -I scripts/copyright-overlap.py [--n 8] [--source ~/Documents/EMyth/markdown]

Compares every N-word window (default 8) in docs/**/*.adoc against the source
markdown, after normalising case and punctuation. Prints each match with its
file and a little context. Short common phrases are expected; long runs are not.
"""
import argparse, pathlib, re, sys

def words(text):
    return re.findall(r"[a-z0-9']+", text.lower())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument("--source", default=str(pathlib.Path.home() / "Documents/EMyth/markdown"))
    ap.add_argument("--docs", default=str(pathlib.Path(__file__).resolve().parent.parent / "docs"))
    a = ap.parse_args()
    src = pathlib.Path(a.source).expanduser()
    files = sorted(src.glob("*.md"))
    if not files:
        sys.exit(f"No source markdown found in {src}")
    grams = set()
    for f in files:
        w = words(f.read_text(errors="ignore"))
        grams.update(tuple(w[i:i + a.n]) for i in range(len(w) - a.n + 1))
    hits = 0
    for page in sorted(pathlib.Path(a.docs).rglob("*.adoc")):
        lines = [l for l in page.read_text().splitlines() if not l.lstrip().startswith(("//", ":"))]
        w = words("\n".join(lines))
        i = 0
        while i <= len(w) - a.n:
            if tuple(w[i:i + a.n]) in grams:
                j = i + a.n
                while j < len(w) and tuple(w[j - a.n + 1:j + 1]) in grams:
                    j += 1
                print(f"{page.name}: {' '.join(w[i:j])}")
                hits += 1
                i = j
            else:
                i += 1
    print(f"\n{hits} overlapping run(s) of {a.n}+ words.")

if __name__ == "__main__":
    main()
