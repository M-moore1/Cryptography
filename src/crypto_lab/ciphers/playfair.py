"""Playfair digraph substitution cipher."""

from __future__ import annotations

from crypto_lab.text import ALPHABET, clean_letters, chunks


def _square(key: str) -> str:
    seen: set[str] = set()
    letters = clean_letters(key).replace("J", "I") + ALPHABET.replace("J", "")
    result = []
    for ch in letters:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)


def _position(square: str, ch: str) -> tuple[int, int]:
    index = square.index("I" if ch == "J" else ch)
    return divmod(index, 5)


def _prepare_plaintext(text: str) -> list[str]:
    letters = clean_letters(text).replace("J", "I")
    pairs: list[str] = []
    i = 0
    while i < len(letters):
        first = letters[i]
        second = letters[i + 1] if i + 1 < len(letters) else "X"
        if first == second:
            pairs.append(first + "X")
            i += 1
        else:
            pairs.append(first + second)
            i += 2
    return pairs


def _transform_pair(pair: str, square: str, direction: int) -> str:
    row1, col1 = _position(square, pair[0])
    row2, col2 = _position(square, pair[1])
    if row1 == row2:
        return square[row1 * 5 + (col1 + direction) % 5] + square[row2 * 5 + (col2 + direction) % 5]
    if col1 == col2:
        return square[((row1 + direction) % 5) * 5 + col1] + square[((row2 + direction) % 5) * 5 + col2]
    return square[row1 * 5 + col2] + square[row2 * 5 + col1]


def playfair_encrypt(plaintext: str, key: str) -> str:
    """Encrypt plaintext using Playfair's 5x5 key square."""

    square = _square(key)
    return "".join(_transform_pair(pair, square, 1) for pair in _prepare_plaintext(plaintext))


def playfair_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt Playfair text. Inserted filler X characters are preserved."""

    square = _square(key)
    return "".join(_transform_pair(pair, square, -1) for pair in chunks(clean_letters(ciphertext), 2))

