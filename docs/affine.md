# Affine Cipher

The affine cipher encrypts each letter number `x` with `E(x) = (a*x + b) mod 26`.

## Implementation

- File: `src/crypto_lab/ciphers/affine.py`
- Functions: `affine_encrypt`, `affine_decrypt`
- `a` must be coprime with 26.
- `b` must be between 0 and 25.

## Example

```bash
python -m crypto_lab.cli affine encrypt "AFFINE CIPHER" -a 5 -b 8
```

## Security

Affine ciphers are monoalphabetic substitutions, so they are vulnerable to frequency analysis.

