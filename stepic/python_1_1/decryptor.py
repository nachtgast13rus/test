decryptor_key = input()
decryptor_cipher = input()
string_cipher = input()
string_decryption = input()

cipher = dict(zip(decryptor_key, decryptor_cipher))
decryptor = dict(zip(decryptor_cipher, decryptor_key))


def cryption(string, cryptor):
    text = list(string)
    for i, let in enumerate(text):
        if let in cryptor:
            text[i] = cryptor[let]
    text = ''.join(text)
    print(text)


cryption(string_cipher, cipher)
cryption(string_decryption, decryptor)

source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
