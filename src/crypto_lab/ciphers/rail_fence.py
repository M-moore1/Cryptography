"""Rail fence transposition cipher."""

from __future__ import annotations


def _rail_pattern(length: int, rails: int) -> list[int]:
    if rails < 2:
        raise ValueError("rails must be at least 2")
    pattern: list[int] = []
    rail = 0
    direction = 1
    for _ in range(length):
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return pattern


def rail_fence_encrypt(plaintext: str, rails: int) -> str:
    """Write text diagonally over rails, then read row by row."""

    pattern = _rail_pattern(len(plaintext), rails)
    rows = [""] * rails
    for ch, rail in zip(plaintext, pattern):
        rows[rail] += ch
    return "".join(rows)


def rail_fence_decrypt(ciphertext: str, rails: int) -> str:
    """Reverse rail fence transposition."""

    pattern = _rail_pattern(len(ciphertext), rails)
    rail_lengths = [pattern.count(rail) for rail in range(rails)]
    rows: list[list[str]] = []
    index = 0
    for length in rail_lengths:
        rows.append(list(ciphertext[index : index + length]))
        index += length
    return "".join(rows[rail].pop(0) for rail in pattern)

