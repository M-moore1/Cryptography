"""Shared text utilities for classical ciphers."""

from __future__ import annotations

import string

ALPHABET = string.ascii_uppercase


def clean_letters(text: str) -> str:
    """Return only A-Z characters from text, uppercased."""

    return "".join(ch for ch in text.upper() if ch in ALPHABET)


def shift_char(ch: str, amount: int) -> str:
    """Shift one alphabetic character while preserving case."""

    alphabet = string.ascii_uppercase if ch.isupper() else string.ascii_lowercase
    if ch not in alphabet:
        return ch
    return alphabet[(alphabet.index(ch) + amount) % 26]


def chunks(text: str, size: int) -> list[str]:
    """Split text into equal-sized chunks, with the final chunk possibly short."""

    if size <= 0:
        raise ValueError("chunk size must be positive")
    return [text[i : i + size] for i in range(0, len(text), size)]

