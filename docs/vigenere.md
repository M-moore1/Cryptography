# Vigenere Cipher

Vigenere improves on Caesar by using a repeated keyword. Each letter of the key determines a Caesar shift for the matching plaintext letter.

## Implementation

- File: `src/crypto_lab/ciphers/vigenere.py`
- Functions: `vigenere_encrypt`, `vigenere_decrypt`
- Non-letters are preserved and do not consume key characters.

## Example

```bash
python -m crypto_lab.cli vigenere encrypt "ATTACK AT DAWN" --key LEMON
python -m crypto_lab.cli vigenere decrypt "LXFOPV EF RNHR" --key LEMON
```

## Security

Vigenere can be broken with key-length analysis and frequency analysis, especially when the key is short or reused.

