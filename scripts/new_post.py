#!/usr/bin/env python3
"""Create a new draft essay for Pelican."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path


ARTICLES_DIR = Path("content/articles")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    return ascii_text.strip("-")


def create_post(title: str) -> Path:
    slug = slugify(title)
    if not slug:
        raise ValueError("The title must contain at least one letter or number.")

    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    path = ARTICLES_DIR / f"{slug}.md"
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")

    today = date.today().isoformat()
    body = (
        f"Title: {title}\n"
        f"Date: {today}\n"
        f"Modified: {today}\n"
        "Category: Ensayos\n"
        "Tags: \n"
        f"Slug: {slug}\n"
        "Summary: \n"
        "Status: draft\n"
        "\n"
        "Escribe aquí el primer párrafo.\n"
    )
    path.write_text(body, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new draft essay.")
    parser.add_argument("title", help="Essay title")
    args = parser.parse_args()

    try:
        path = create_post(args.title)
    except (FileExistsError, ValueError) as exc:
        print(exc, file=sys.stderr)
        return 1

    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
