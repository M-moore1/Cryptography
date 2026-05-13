"""Caesar cipher.

The Caesar cipher shifts each letter by a fixed number of positions. It is one
of the simplest substitution ciphers and can be broken by trying all 26 shifts.
"""

from __future__ import annotations

from crypto_lab.text import shift_char


def caesar_encrypt(plaintext: str, shift: int) -> str:
    """Encrypt text with a Caesar shift."""

    return "".join(shift_char(ch, shift) for ch in plaintext)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt text encrypted with the same Caesar shift."""

    return caesar_encrypt(ciphertext, -shift)


def brute_force_caesar(ciphertext: str) -> dict[int, str]:
    """Return every possible Caesar decryption keyed by shift."""

    return {shift: caesar_decrypt(ciphertext, shift) for shift in range(26)}

