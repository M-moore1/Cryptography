# Caesar Cipher

The Caesar cipher shifts every alphabetic character by a fixed amount. With a shift of `3`, `A` becomes `D`, `B` becomes `E`, and so on.

## Implementation

- File: `src/crypto_lab/ciphers/caesar.py`
- Functions: `caesar_encrypt`, `caesar_decrypt`, `brute_force_caesar`
- Non-letters are preserved.
- Letter case is preserved.

## Example

```bash
python -m crypto_lab.cli caesar encrypt "Attack at dawn" --shift 3
python -m crypto_lab.cli caesar decrypt "Dwwdfn dw gdzq" --shift 3
```

## Security

The Caesar cipher has only 26 possible shifts, so brute force is immediate.

