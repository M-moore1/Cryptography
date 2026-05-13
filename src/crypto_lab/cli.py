"""Command-line interface for Crypto Lab."""

from __future__ import annotations

import argparse

from crypto_lab.analysis.frequency import frequency_table
from crypto_lab.ciphers import (
    affine_decrypt,
    affine_encrypt,
    atbash,
    caesar_decrypt,
    caesar_encrypt,
    columnar_decrypt,
    columnar_encrypt,
    rail_fence_decrypt,
    rail_fence_encrypt,
    substitution_decrypt,
    substitution_encrypt,
    vigenere_decrypt,
    vigenere_encrypt,
    xor_decrypt_from_hex,
    xor_encrypt_to_hex,
)
from crypto_lab.ciphers.caesar import brute_force_caesar
from crypto_lab.protocols.hashing import hash_text, hmac_text


def _print(value: object) -> None:
    print(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="crypto-lab", description="Educational cryptography toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    caesar = subparsers.add_parser("caesar", help="Encrypt/decrypt Caesar cipher")
    caesar.add_argument("mode", choices=["encrypt", "decrypt", "bruteforce"])
    caesar.add_argument("text")
    caesar.add_argument("--shift", type=int, default=3)

    vigenere = subparsers.add_parser("vigenere", help="Encrypt/decrypt Vigenere cipher")
    vigenere.add_argument("mode", choices=["encrypt", "decrypt"])
    vigenere.add_argument("text")
    vigenere.add_argument("--key", required=True)

    affine = subparsers.add_parser("affine", help="Encrypt/decrypt affine cipher")
    affine.add_argument("mode", choices=["encrypt", "decrypt"])
    affine.add_argument("text")
    affine.add_argument("-a", type=int, required=True)
    affine.add_argument("-b", type=int, required=True)

    atbash_parser = subparsers.add_parser("atbash", help="Apply Atbash substitution")
    atbash_parser.add_argument("text")

    substitution = subparsers.add_parser("substitution", help="Monoalphabetic substitution")
    substitution.add_argument("mode", choices=["encrypt", "decrypt"])
    substitution.add_argument("text")
    substitution.add_argument("--alphabet", required=True)

    rail = subparsers.add_parser("rail-fence", help="Rail fence transposition")
    rail.add_argument("mode", choices=["encrypt", "decrypt"])
    rail.add_argument("text")
    rail.add_argument("--rails", type=int, required=True)

    columnar = subparsers.add_parser("columnar", help="Columnar transposition")
    columnar.add_argument("mode", choices=["encrypt", "decrypt"])
    columnar.add_argument("text")
    columnar.add_argument("--key", required=True)

    xor = subparsers.add_parser("xor", help="Repeating-key XOR")
    xor.add_argument("mode", choices=["encrypt", "decrypt"])
    xor.add_argument("text")
    xor.add_argument("--key", required=True)

    hashing = subparsers.add_parser("hash", help="Hash text")
    hashing.add_argument("text")
    hashing.add_argument("--algorithm", default="sha256")

    hmac_parser = subparsers.add_parser("hmac", help="HMAC text")
    hmac_parser.add_argument("text")
    hmac_parser.add_argument("--key", required=True)
    hmac_parser.add_argument("--algorithm", default="sha256")

    frequency = subparsers.add_parser("frequency", help="Letter frequency analysis")
    frequency.add_argument("text")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    match args.command:
        case "caesar":
            if args.mode == "encrypt":
                _print(caesar_encrypt(args.text, args.shift))
            elif args.mode == "decrypt":
                _print(caesar_decrypt(args.text, args.shift))
            else:
                for shift, candidate in brute_force_caesar(args.text).items():
                    _print(f"{shift:02d}: {candidate}")
        case "vigenere":
            _print(vigenere_encrypt(args.text, args.key) if args.mode == "encrypt" else vigenere_decrypt(args.text, args.key))
        case "affine":
            _print(affine_encrypt(args.text, args.a, args.b) if args.mode == "encrypt" else affine_decrypt(args.text, args.a, args.b))
        case "atbash":
            _print(atbash(args.text))
        case "substitution":
            func = substitution_encrypt if args.mode == "encrypt" else substitution_decrypt
            _print(func(args.text, args.alphabet))
        case "rail-fence":
            func = rail_fence_encrypt if args.mode == "encrypt" else rail_fence_decrypt
            _print(func(args.text, args.rails))
        case "columnar":
            func = columnar_encrypt if args.mode == "encrypt" else columnar_decrypt
            _print(func(args.text, args.key))
        case "xor":
            func = xor_encrypt_to_hex if args.mode == "encrypt" else xor_decrypt_from_hex
            _print(func(args.text, args.key))
        case "hash":
            _print(hash_text(args.text, args.algorithm))
        case "hmac":
            _print(hmac_text(args.text, args.key, args.algorithm))
        case "frequency":
            for letter, count, percent in frequency_table(args.text):
                _print(f"{letter}: {count:3d} {percent:5.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

