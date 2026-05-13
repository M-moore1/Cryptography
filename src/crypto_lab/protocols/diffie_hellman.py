"""Small Diffie-Hellman key exchange demonstration."""

from __future__ import annotations

from dataclasses import dataclass
from secrets import randbelow


@dataclass(frozen=True)
class DiffieHellmanParty:
    """One participant in a Diffie-Hellman exchange."""

    private_key: int
    public_key: int
    prime: int
    generator: int

    @classmethod
    def create(cls, prime: int = 2_147_483_647, generator: int = 5) -> "DiffieHellmanParty":
        """Create a party using a Mersenne prime suitable for demonstration."""

        private_key = randbelow(prime - 2) + 2
        public_key = pow(generator, private_key, prime)
        return cls(private_key, public_key, prime, generator)

    def shared_secret(self, other_public_key: int) -> int:
        """Compute the shared secret from the other party's public key."""

        if not 1 < other_public_key < self.prime:
            raise ValueError("public key must be between 2 and prime - 1")
        return pow(other_public_key, self.private_key, self.prime)

