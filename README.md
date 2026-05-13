# Crypto Lab

Crypto Lab is a complete educational cryptography project. It includes classical ciphers, transposition ciphers, cryptanalysis helpers, hashing/HMAC utilities, and small demonstrations of RSA and Diffie-Hellman.

This project is for learning. Classical ciphers, repeating-key XOR, and the RSA module here are not production-safe. For real security work, use vetted libraries and modern authenticated encryption.

## Contents

- Classical substitution: Caesar, Atbash, Vigenere, Affine, Monoalphabetic Substitution, Playfair, Hill
- Transposition: Rail Fence, Columnar Transposition
- Byte-oriented demo: Repeating-key XOR
- Modern concepts: SHA hashes, HMAC, Diffie-Hellman, toy RSA
- Cryptanalysis: frequency tables, Caesar brute force, English-likeness scoring
- Documentation: one guide per cipher/protocol in `docs/`
- Tests: regression tests in `tests/`
- CLI: `crypto-lab`

## Quick Start

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
python3 -m crypto_lab.cli caesar encrypt "Attack at dawn" --shift 3
python3 -m crypto_lab.cli vigenere decrypt "LXFOPV EF RNHR" --key LEMON
python3 examples/demo.py
```

For editable CLI usage:

```bash
python3 -m pip install -e .
crypto-lab hash "hello"
crypto-lab caesar bruteforce "Dwwdfn dw gdzq"
```

## Project Layout

```text
src/crypto_lab/
  ciphers/       Classical and educational cipher implementations
  protocols/     Hashing, HMAC, Diffie-Hellman, and toy RSA demos
  analysis/      Frequency analysis and scoring helpers
  cli.py         Command-line interface
docs/            Explanations, examples, strengths, and weaknesses
examples/        Small runnable demonstrations
tests/           Pytest test suite
```

## Example Python Usage

```python
from crypto_lab.ciphers import caesar_encrypt, vigenere_decrypt
from crypto_lab.protocols import hash_text

print(caesar_encrypt("Attack at dawn", 3))
print(vigenere_decrypt("LXFOPV EF RNHR", "LEMON"))
print(hash_text("hello"))
```

## Safety Notes

- Caesar, Atbash, Vigenere, Affine, Substitution, Playfair, Hill, Rail Fence, and Columnar Transposition are historical ciphers.
- Repeating-key XOR is breakable if the key repeats or plaintext is predictable.
- The RSA implementation omits padding, serialization, side-channel defenses, and many production requirements.
- Hashing is not encryption. A hash digest cannot be decrypted.
- HMAC provides integrity/authenticity when both parties already share a secret key.
