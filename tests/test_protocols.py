from crypto_lab.protocols.diffie_hellman import DiffieHellmanParty
from crypto_lab.protocols.hashing import hash_text, hmac_text
from crypto_lab.protocols.rsa_demo import rsa_generate_keypair


def test_hash_text_sha256():
    assert hash_text("hello") == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


def test_hmac_text_is_stable():
    assert hmac_text("message", "key") == hmac_text("message", "key")


def test_diffie_hellman_shared_secret_matches():
    alice = DiffieHellmanParty.create()
    bob = DiffieHellmanParty.create(prime=alice.prime, generator=alice.generator)
    assert alice.shared_secret(bob.public_key) == bob.shared_secret(alice.public_key)


def test_rsa_integer_round_trip():
    keypair = rsa_generate_keypair(bits=128)
    message = 42
    assert keypair.decrypt_int(keypair.encrypt_int(message)) == message

