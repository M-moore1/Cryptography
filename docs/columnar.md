# Columnar Transposition

Columnar transposition writes text into rows under a keyword, then reads columns according to the alphabetical order of the keyword letters.

## Implementation

- File: `src/crypto_lab/ciphers/columnar.py`
- Functions: `columnar_encrypt`, `columnar_decrypt`
- Encryption pads with `X` by default to fill the final row.

## Example

```bash
python -m crypto_lab.cli columnar encrypt "WEAREDISCOVERED" --key ZEBRA
```

## Security

Columnar transposition is stronger than very simple transpositions but remains breakable with anagramming and known-plaintext clues.

