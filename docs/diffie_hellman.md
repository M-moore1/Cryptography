# Diffie-Hellman Key Exchange

Diffie-Hellman lets two parties create the same shared secret over an insecure channel.

## Implementation

- File: `src/crypto_lab/protocols/diffie_hellman.py`
- Class: `DiffieHellmanParty`
- Uses modular exponentiation: public key is `g^private mod p`.

## Example

```python
from crypto_lab.protocols import DiffieHellmanParty

alice = DiffieHellmanParty.create()
bob = DiffieHellmanParty.create(prime=alice.prime, generator=alice.generator)
assert alice.shared_secret(bob.public_key) == bob.shared_secret(alice.public_key)
```

## Security

Real systems use carefully selected groups or elliptic curves, authenticate the exchange, and derive symmetric keys with a KDF.

