# Hill Cipher

The Hill cipher uses matrix multiplication modulo 26. This project implements the common 2x2 version.

## Implementation

- File: `src/crypto_lab/ciphers/hill.py`
- Functions: `hill_encrypt`, `hill_decrypt`
- The determinant of the key matrix must be coprime with 26.
- Text is cleaned to A-Z and padded with `X` if needed.

## Example

```python
from crypto_lab.ciphers import hill_encrypt, hill_decrypt

key = ((3, 3), (2, 5))
ciphertext = hill_encrypt("HELP", key)
print(ciphertext)
print(hill_decrypt(ciphertext, key))
```

## Security

Hill ciphers are vulnerable to known-plaintext attacks because enough plaintext/ciphertext pairs reveal the matrix.

