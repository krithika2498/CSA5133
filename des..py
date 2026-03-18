

def xor(a, b):
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result


def text_to_bin(text):
    return ''.join(format(ord(i), '08b') for i in text)


def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)


# ===== User Input =====
plain = input("Enter message: ")
key = input("Enter 8-bit binary key (example 10101010): ")

plain_bin = text_to_bin(plain)

# repeat key to match length
key = key * (len(plain_bin)//len(key) + 1)
key = key[:len(plain_bin)]

cipher_bin = xor(plain_bin, key)
cipher_text = bin_to_text(cipher_bin)

print("Encrypted:", cipher_text)

# decrypt
decrypt_bin = xor(cipher_bin, key)
decrypt_text = bin_to_text(decrypt_bin)

print("Decrypted:", decrypt_text)
