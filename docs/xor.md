# Repeating-Key XOR

XOR combines bytes with a key. In this project, the key repeats across the message.

## Implementation

- File: `src/crypto_lab/ciphers/xor.py`
- Functions: `xor_bytes`, `xor_encrypt_to_hex`, `xor_decrypt_from_hex`
- Ciphertext is represented as hex for readable CLI output.

## Example

```bash
python -m crypto_lab.cli xor encrypt "secret" --key key
python -m crypto_lab.cli xor decrypt "18000a19000d" --key key
```

## Security

Repeating-key XOR leaks patterns. Modern stream ciphers avoid this by using secure keystream generation and never reusing nonce/key combinations.

