"""Columnar transposition cipher."""

from __future__ import annotations

import math


def _column_order(key: str) -> list[int]:
    cleaned = key.upper()
    if not cleaned:
        raise ValueError("key must not be empty")
    return [index for index, _ in sorted(enumerate(cleaned), key=lambda item: (item[1], item[0]))]


def columnar_encrypt(plaintext: str, key: str, pad: str = "X") -> str:
    """Encrypt by writing rows under a keyword and reading sorted columns."""

    if len(pad) != 1:
        raise ValueError("pad must be one character")
    width = len(key)
    order = _column_order(key)
    padded = plaintext
    while len(padded) % width:
        padded += pad
    rows = [padded[i : i + width] for i in range(0, len(padded), width)]
    return "".join("".join(row[column] for row in rows) for column in order)


def columnar_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt a padded columnar transposition message."""

    width = len(key)
    order = _column_order(key)
    height = math.ceil(len(ciphertext) / width)
    columns: dict[int, str] = {}
    index = 0
    for column in order:
        columns[column] = ciphertext[index : index + height]
        index += height
    output = []
    for row in range(height):
        for column in range(width):
            if row < len(columns[column]):
                output.append(columns[column][row])
    return "".join(output)

