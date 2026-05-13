from crypto_lab.ciphers import (
    affine_decrypt,
    affine_encrypt,
    atbash,
    caesar_decrypt,
    caesar_encrypt,
    columnar_decrypt,
    columnar_encrypt,
    hill_decrypt,
    hill_encrypt,
    playfair_decrypt,
    playfair_encrypt,
    rail_fence_decrypt,
    rail_fence_encrypt,
    substitution_decrypt,
    substitution_encrypt,
    vigenere_decrypt,
    vigenere_encrypt,
    xor_decrypt_from_hex,
    xor_encrypt_to_hex,
)


def test_caesar_round_trip():
    encrypted = caesar_encrypt("Attack at dawn!", 5)
    assert encrypted == "Fyyfhp fy ifbs!"
    assert caesar_decrypt(encrypted, 5) == "Attack at dawn!"


def test_vigenere_round_trip():
    encrypted = vigenere_encrypt("ATTACK AT DAWN", "LEMON")
    assert encrypted == "LXFOPV EF RNHR"
    assert vigenere_decrypt(encrypted, "LEMON") == "ATTACK AT DAWN"


def test_atbash():
    assert atbash("Attack!") == "Zggzxp!"


def test_affine_round_trip():
    encrypted = affine_encrypt("AFFINE CIPHER", 5, 8)
    assert encrypted == "IHHWVC SWFRCP"
    assert affine_decrypt(encrypted, 5, 8) == "AFFINE CIPHER"


def test_substitution_round_trip():
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
    encrypted = substitution_encrypt("Hello", alphabet)
    assert substitution_decrypt(encrypted, alphabet) == "Hello"


def test_rail_fence_round_trip():
    encrypted = rail_fence_encrypt("WEAREDISCOVEREDFLEEATONCE", 3)
    assert encrypted == "WECRLTEERDSOEEFEAOCAIVDEN"
    assert rail_fence_decrypt(encrypted, 3) == "WEAREDISCOVEREDFLEEATONCE"


def test_columnar_round_trip():
    encrypted = columnar_encrypt("WEAREDISCOVERED", "ZEBRA")
    assert columnar_decrypt(encrypted, "ZEBRA").startswith("WEAREDISCOVERED")


def test_playfair_known_example():
    encrypted = playfair_encrypt("Hide the gold in the tree stump", "playfair example")
    assert encrypted == "BMODZBXDNABEKUDMUIXMMOUVIF"
    assert playfair_decrypt(encrypted, "playfair example") == "HIDETHEGOLDINTHETREXESTUMP"


def test_hill_round_trip():
    key = ((3, 3), (2, 5))
    encrypted = hill_encrypt("HELP", key)
    assert encrypted == "HIAT"
    assert hill_decrypt(encrypted, key) == "HELP"


def test_xor_round_trip():
    encrypted = xor_encrypt_to_hex("secret", "key")
    assert xor_decrypt_from_hex(encrypted, "key") == "secret"

