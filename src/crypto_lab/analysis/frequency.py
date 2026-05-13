"""Letter frequency analysis utilities."""

from __future__ import annotations

from collections import Counter

from crypto_lab.text import ALPHABET, clean_letters

ENGLISH_FREQUENCY_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def frequency_table(text: str) -> list[tuple[str, int, float]]:
    """Return A-Z counts and percentages sorted from most to least common."""

    letters = clean_letters(text)
    total = len(letters) or 1
    counts = Counter(letters)
    rows = [(letter, counts[letter], counts[letter] / total * 100) for letter in ALPHABET]
    return sorted(rows, key=lambda row: (-row[1], row[0]))


def score_english(text: str) -> float:
    """Score text by how closely its most common letters resemble English."""

    observed = "".join(letter for letter, count, _ in frequency_table(text) if count)
    return sum(max(0, 26 - abs(ENGLISH_FREQUENCY_ORDER.index(ch) - index)) for index, ch in enumerate(observed[:26]))

