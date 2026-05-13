"""Monoalphabetic substitution cipher."""

from __future__ import annotations

import string

from crypto_lab.text import ALPHABET


def _validate_alphabet(cipher_alphabet: str) -> str:
    normalized = cipher_alphabet.upper()
    if len(normalized) != 26 or set(normalized) != set(ALPHABET):
        raise ValueError("cipher alphabet must contain each A-Z letter exactly once")
    return normalized


def substitution_encrypt(plaintext: str, cipher_alphabet: str) -> str:
    """Encrypt using a 26-letter replacement alphabet."""

    cipher = _validate_alphabet(cipher_alphabet)
    upper_map = str.maketrans(ALPHABET, cipher)
    lower_map = str.maketrans(string.ascii_lowercase, cipher.lower())
    return plaintext.translate(upper_map).translate(lower_map)


def substitution_decrypt(ciphertext: str, cipher_alphabet: str) -> str:
    """Decrypt using the replacement alphabet from encryption."""

    cipher = _validate_alphabet(cipher_alphabet)
    upper_map = str.maketrans(cipher, ALPHABET)
    lower_map = str.maketrans(cipher.lower(), string.ascii_lowercase)
    return ciphertext.translate(upper_map).translate(lower_map)

