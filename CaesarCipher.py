import string
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def gen_key(alphabet):
    key = int(input("Enter your shift key: "))
    return key

def make_alphabet(key):
    split1, split2 = alphabet[:key], alphabet[key:]
    new_alphabet = split2 + split1
    return new_alphabet

def enc(message, key):
    cipher_text = ''
    a = make_alphabet(key)
    message = message.lower()
    for letter in message:
        if letter in alphabet:
            cipher_text += a[alphabet.index(letter)]
        else:
            cipher_text += message[message.index(letter)]
    return cipher_text

def dec(cipher_text, key):
    message = ''
    a = make_alphabet(key)
    for letter in cipher_text:
        if letter in a:
            message += alphabet[a.index(letter)]
        else:
            message += letter
            continue
    return message

def main():
    print("-Welcome to the Caesar Cipher-")
    
    while(True):
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = int(input("Choose an option: "))

        if (choice == 1):
            message = input("Enter message: ")
            key = gen_key(alphabet)
            cipher_text = enc(message, key)
            print(cipher_text)
        elif (choice == 2):
            cipher_text = input("Enter cipher text: ")
            key = gen_key(alphabet)
            message = dec(cipher_text, key)
            print(message)
        elif (choice == 3):
            break

if __name__ == "__main__":
    main()
