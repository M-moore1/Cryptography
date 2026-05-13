# Atbash Cipher

Atbash maps the alphabet to itself in reverse: `A` becomes `Z`, `B` becomes `Y`, and so on.

## Implementation

- File: `src/crypto_lab/ciphers/atbash.py`
- Function: `atbash`
- The same function encrypts and decrypts.

## Example

```bash
python -m crypto_lab.cli atbash "Attack at dawn"
```

## Security

Atbash has no secret key, so it offers no real secrecy.

