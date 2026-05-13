# Frequency Analysis

Frequency analysis studies how often symbols occur in ciphertext. Many classical ciphers leak enough language structure to attack this way.

## Implementation

- File: `src/crypto_lab/analysis/frequency.py`
- Functions: `frequency_table`, `score_english`
- CLI command: `frequency`

## Example

```bash
python -m crypto_lab.cli frequency "WKLV LV D FDHVDU PHVVDJH"
```

## Use

Frequency analysis is especially useful against Caesar, affine, and monoalphabetic substitution ciphers. It is less direct against transposition ciphers because the letters are preserved but reordered.

