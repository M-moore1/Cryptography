"""Hashing and HMAC helpers using Python's standard library."""

from __future__ import annotations

import hashlib
import hmac
from pathlib import Path

SUPPORTED_HASHES = sorted(hashlib.algorithms_guaranteed)


def hash_text(text: str, algorithm: str = "sha256", encoding: str = "utf-8") -> str:
    """Hash text and return a hexadecimal digest."""

    digest = hashlib.new(algorithm)
    digest.update(text.encode(encoding))
    return digest.hexdigest()


def hash_file(path: str | Path, algorithm: str = "sha256", chunk_size: int = 65536) -> str:
    """Hash a file incrementally and return a hexadecimal digest."""

    digest = hashlib.new(algorithm)
    with Path(path).open("rb") as file:
        for block in iter(lambda: file.read(chunk_size), b""):
            digest.update(block)
    return digest.hexdigest()


def hmac_text(message: str, key: str, algorithm: str = "sha256", encoding: str = "utf-8") -> str:
    """Create an HMAC for integrity and authenticity checks."""

    return hmac.new(key.encode(encoding), message.encode(encoding), algorithm).hexdigest()

