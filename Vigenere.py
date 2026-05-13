"""Legacy interactive wrapper for the Vigenere cipher.

The maintained implementation lives in `src/crypto_lab/ciphers/vigenere.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from crypto_lab.ciphers import vigenere_decrypt, vigenere_encrypt  # noqa: E402


def main() -> None:
    print("-Welcome to the Vigenere Cipher-")
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            message = input("Enter message: ")
            key = input("Enter key word: ")
            print(vigenere_encrypt(message, key))
        elif choice == "2":
            ciphertext = input("Enter cipher text: ")
            key = input("Enter key word: ")
            print(vigenere_decrypt(ciphertext, key))
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

