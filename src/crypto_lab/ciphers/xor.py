"""Repeating-key XOR cipher.

Repeating-key XOR is useful for learning stream-cipher ideas, but it is not
secure against serious attackers when used directly.
"""

from __future__ import annotations


def xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR bytes with a repeating key."""

    if not key:
        raise ValueError("key must not be empty")
    return bytes(byte ^ key[index % len(key)] for index, byte in enumerate(data))


def xor_encrypt_to_hex(plaintext: str, key: str, encoding: str = "utf-8") -> str:
    """Encrypt text with repeating-key XOR and return hex."""

    return xor_bytes(plaintext.encode(encoding), key.encode(encoding)).hex()


def xor_decrypt_from_hex(ciphertext_hex: str, key: str, encoding: str = "utf-8") -> str:
    """Decrypt repeating-key XOR hex back to text."""

    return xor_bytes(bytes.fromhex(ciphertext_hex), key.encode(encoding)).decode(encoding)

