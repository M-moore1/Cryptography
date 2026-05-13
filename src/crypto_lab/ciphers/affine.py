"""Affine substitution cipher."""

from __future__ import annotations

import math

from crypto_lab.text import ALPHABET


def _validate_key(a: int, b: int) -> None:
    if math.gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26; valid examples include 5, 7, 11, 17")
    if not 0 <= b < 26:
        raise ValueError("b must be between 0 and 25")


def _mod_inverse(value: int, modulus: int) -> int:
    for candidate in range(modulus):
        if (value * candidate) % modulus == 1:
            return candidate
    raise ValueError("no modular inverse exists")


def _transform_char(ch: str, a: int, b: int, decrypt: bool) -> str:
    if ch.upper() not in ALPHABET:
        return ch
    base = ord("A") if ch.isupper() else ord("a")
    x = ord(ch) - base
    if decrypt:
        value = (_mod_inverse(a, 26) * (x - b)) % 26
    else:
        value = (a * x + b) % 26
    return chr(value + base)


def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    """Encrypt with E(x) = (a*x + b) mod 26."""

    _validate_key(a, b)
    return "".join(_transform_char(ch, a, b, False) for ch in plaintext)


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    """Decrypt an affine cipher."""

    _validate_key(a, b)
    return "".join(_transform_char(ch, a, b, True) for ch in ciphertext)

