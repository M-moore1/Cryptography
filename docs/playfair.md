# Playfair Cipher

Playfair encrypts pairs of letters using a 5x5 square built from a keyword. `I` and `J` share one cell.

## Implementation

- File: `src/crypto_lab/ciphers/playfair.py`
- Functions: `playfair_encrypt`, `playfair_decrypt`
- Repeated letters in a pair are separated with `X`.
- Odd-length messages are padded with `X`.

## Example

```python
from crypto_lab.ciphers import playfair_encrypt

print(playfair_encrypt("Hide the gold in the tree stump", "playfair example"))
```

## Security

Playfair hides single-letter frequency better than monoalphabetic substitution, but digraph patterns still leak enough structure for attacks.

