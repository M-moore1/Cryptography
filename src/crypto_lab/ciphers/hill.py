"""Two-by-two Hill cipher over the English alphabet."""

from __future__ import annotations

import math

from crypto_lab.text import clean_letters

Matrix2x2 = tuple[tuple[int, int], tuple[int, int]]


def _determinant(matrix: Matrix2x2) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def _mod_inverse(value: int, modulus: int) -> int:
    value %= modulus
    for candidate in range(modulus):
        if (value * candidate) % modulus == 1:
            return candidate
    raise ValueError("matrix determinant has no modular inverse")


def _validate_key(matrix: Matrix2x2) -> None:
    if math.gcd(_determinant(matrix), 26) != 1:
        raise ValueError("matrix determinant must be coprime with 26")


def _inverse_key(matrix: Matrix2x2) -> Matrix2x2:
    det_inv = _mod_inverse(_determinant(matrix), 26)
    return (
        ((matrix[1][1] * det_inv) % 26, (-matrix[0][1] * det_inv) % 26),
        ((-matrix[1][0] * det_inv) % 26, (matrix[0][0] * det_inv) % 26),
    )


def _apply(text: str, matrix: Matrix2x2) -> str:
    letters = clean_letters(text)
    if len(letters) % 2:
        letters += "X"
    output = []
    for a, b in zip(letters[0::2], letters[1::2]):
        x, y = ord(a) - ord("A"), ord(b) - ord("A")
        output.append(chr((matrix[0][0] * x + matrix[0][1] * y) % 26 + ord("A")))
        output.append(chr((matrix[1][0] * x + matrix[1][1] * y) % 26 + ord("A")))
    return "".join(output)


def hill_encrypt(plaintext: str, matrix: Matrix2x2) -> str:
    """Encrypt using a 2x2 Hill key matrix."""

    _validate_key(matrix)
    return _apply(plaintext, matrix)


def hill_decrypt(ciphertext: str, matrix: Matrix2x2) -> str:
    """Decrypt using the inverse of the Hill key matrix."""

    _validate_key(matrix)
    return _apply(ciphertext, _inverse_key(matrix))

