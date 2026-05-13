# RSA Demo

RSA is a public-key cryptosystem based on modular exponentiation and the difficulty of factoring large numbers.

## Implementation

- File: `src/crypto_lab/protocols/rsa_demo.py`
- Functions/classes: `rsa_generate_keypair`, `RSAKeyPair`
- Includes Miller-Rabin probable prime testing.
- Supports integer encryption/decryption only.

## Example

```python
from crypto_lab.protocols import rsa_generate_keypair

keypair = rsa_generate_keypair(bits=128)
ciphertext = keypair.encrypt_int(42)
print(keypair.decrypt_int(ciphertext))
```

## Security

This module is a toy. Production RSA requires secure padding such as OAEP/PSS, large keys, constant-time operations, careful parsing, and mature libraries.

