"""Vigenere cipher."""

from __future__ import annotations

from crypto_lab.text import ALPHABET


def _key_shifts(key: str) -> list[int]:
    shifts = [ALPHABET.index(ch) for ch in key.upper() if ch in ALPHABET]
    if not shifts:
        raise ValueError("key must contain at least one alphabetic character")
    return shifts


def _transform(text: str, key: str, direction: int) -> str:
    shifts = _key_shifts(key)
    output: list[str] = []
    used = 0
    for ch in text:
        if ch.upper() not in ALPHABET:
            output.append(ch)
            continue
        base = ord("A") if ch.isupper() else ord("a")
        shift = shifts[used % len(shifts)] * direction
        output.append(chr((ord(ch) - base + shift) % 26 + base))
        used += 1
    return "".join(output)


def vigenere_encrypt(plaintext: str, key: str) -> str:
    """Encrypt text with a repeated-key Vigenere cipher."""

    return _transform(plaintext, key, 1)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt text with a repeated-key Vigenere cipher."""

    return _transform(ciphertext, key, -1)

