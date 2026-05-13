"""Atbash cipher."""

from __future__ import annotations

import string


def atbash(text: str) -> str:
    """Mirror A-Z and a-z across the alphabet."""

    upper = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[::-1])
    lower = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    return text.translate(upper).translate(lower)

