"""Toy RSA implementation for understanding the algorithm.

Use a vetted library such as cryptography or PyNaCl for real applications. This
module deliberately stays small so the math is visible.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from secrets import randbits, randbelow


@dataclass(frozen=True)
class RSAKeyPair:
    """RSA public and private values."""

    public_exponent: int
    private_exponent: int
    modulus: int
    p: int
    q: int

    def encrypt_int(self, message: int) -> int:
        """Encrypt an integer smaller than the modulus."""

        if not 0 <= message < self.modulus:
            raise ValueError("message integer must be between 0 and modulus - 1")
        return pow(message, self.public_exponent, self.modulus)

    def decrypt_int(self, ciphertext: int) -> int:
        """Decrypt an integer ciphertext."""

        return pow(ciphertext, self.private_exponent, self.modulus)


def _is_probable_prime(number: int, rounds: int = 12) -> bool:
    if number < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if number in small_primes:
        return True
    if any(number % prime == 0 for prime in small_primes):
        return False

    d = number - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(rounds):
        a = randbelow(number - 3) + 2
        x = pow(a, d, number)
        if x in (1, number - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True


def _generate_prime(bits: int) -> int:
    while True:
        candidate = randbits(bits) | (1 << bits - 1) | 1
        if _is_probable_prime(candidate):
            return candidate


def rsa_generate_keypair(bits: int = 512, public_exponent: int = 65537) -> RSAKeyPair:
    """Generate a small RSA key pair for demonstrations."""

    if bits < 128:
        raise ValueError("use at least 128 bits for the demo key")

    half = bits // 2
    while True:
        p = _generate_prime(half)
        q = _generate_prime(bits - half)
        if p == q:
            continue
        phi = (p - 1) * (q - 1)
        if gcd(public_exponent, phi) == 1:
            break

    modulus = p * q
    private_exponent = pow(public_exponent, -1, phi)
    return RSAKeyPair(public_exponent, private_exponent, modulus, p, q)

