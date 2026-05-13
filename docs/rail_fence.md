# Rail Fence Cipher

Rail fence is a transposition cipher. It writes characters in a zig-zag over several rails, then reads each rail in order.

## Implementation

- File: `src/crypto_lab/ciphers/rail_fence.py`
- Functions: `rail_fence_encrypt`, `rail_fence_decrypt`
- Requires at least two rails.

## Example

```bash
python -m crypto_lab.cli rail-fence encrypt "WEAREDISCOVEREDFLEEATONCE" --rails 3
```

## Security

It rearranges letters but does not hide frequency information. It is easily attacked by testing rail counts.

