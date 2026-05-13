"""Small tour of the Crypto Lab package."""

from crypto_lab.ciphers import caesar_encrypt, rail_fence_encrypt, vigenere_encrypt
from crypto_lab.protocols import DiffieHellmanParty, hash_text


def main() -> None:
    print("Caesar:", caesar_encrypt("Meet at midnight", 7))
    print("Vigenere:", vigenere_encrypt("Meet at midnight", "ORBIT"))
    print("Rail fence:", rail_fence_encrypt("MEETATMIDNIGHT", 3))
    print("SHA-256:", hash_text("cryptography"))

    alice = DiffieHellmanParty.create()
    bob = DiffieHellmanParty.create(prime=alice.prime, generator=alice.generator)
    print("DH shared secrets match:", alice.shared_secret(bob.public_key) == bob.shared_secret(alice.public_key))


if __name__ == "__main__":
    main()

