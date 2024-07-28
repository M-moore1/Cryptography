alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key_matrix = []

################################################################
#                       Support Functions                      #
def make_alphabet(key):
    split1, split2 = alphabet[:key], alphabet[key:]
    new_alphabet = split2 + split1
    return new_alphabet

def make_key_matrix():
    for i in range(26):
        j = make_alphabet(i)
        key_matrix.append(j)
    return key_matrix
################################################################

################################################################
#                       Key Generation                         #
def gen_key(message, key):
    key = key.lower()
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
################################################################

################################################################
#                          Encryption                          #
def enc(message, key):
    message = message.lower()
    cipher_text = ''
    for m, k in zip(message, key):
        if (m in alphabet):
            m_index = alphabet.index(m)
            k_index = alphabet.index(k)
            cipher_text += key_matrix[m_index][k_index]
        else:
            cipher_text += m
    return cipher_text
################################################################

################################################################
#                          Decryption                          #
def dec(cipher_text, key):
    cipher_text = cipher_text.lower()
    message = ''
    for c, k in zip(cipher_text, key):
        for row in key_matrix:
            if (row[0] == k and k in alphabet):
                index = row.index(c)
                message += alphabet[index]
            else:
                message += c
    return message
################################################################

def main():
    make_key_matrix()
    print("-Welcome to the Vigenere Cipher-")
    
    while(True):
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = int(input("Choose an option: "))

        if (choice == 1):
            message = input("Enter message: ")
            key_word = input("Enter key word: ")
            key = gen_key(message, key_word)
            cipher_text = enc(message, key)
            print(cipher_text)
        elif (choice == 2):
            cipher_text = input("Enter cipher text: ")
            key_word = input("Enter key word: ")
            key = gen_key(message, key_word)
            #message = dec(cipher_text, key)
            print(message)
        elif (choice == 3):
            break

if __name__ == "__main__":
    main()
