# Hashing and HMAC

Hash functions produce fixed-size digests. HMAC combines a hash function with a secret key to authenticate a message.

## Implementation

- File: `src/crypto_lab/protocols/hashing.py`
- Functions: `hash_text`, `hash_file`, `hmac_text`
- Uses Python's standard `hashlib` and `hmac` modules.

## Example

```bash
python -m crypto_lab.cli hash "hello"
python -m crypto_lab.cli hmac "message" --key "shared-secret"
```

## Security

Hashes do not encrypt data. Use password hashing algorithms such as Argon2, bcrypt, or scrypt for passwords; fast hashes like SHA-256 are not enough by themselves.

