# Monoalphabetic Substitution

This cipher replaces each plaintext letter with a corresponding letter from a shuffled alphabet.

## Implementation

- File: `src/crypto_lab/ciphers/substitution.py`
- Functions: `substitution_encrypt`, `substitution_decrypt`
- The replacement alphabet must contain every A-Z letter exactly once.

## Example

```bash
python -m crypto_lab.cli substitution encrypt "HELLO" --alphabet QWERTYUIOPASDFGHJKLZXCVBNM
```

## Security

The key space is large, but letter frequencies and word patterns usually reveal the mapping.

