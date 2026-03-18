
def des_encrypt(text, key):
    result = ""
    for i in range(len(text)):
        t = ord(text[i])
        k = ord(key[i % len(key)])
        result += chr((t + k) % 256)
    return result


def des_decrypt(cipher, key):
    result = ""
    for i in range(len(cipher)):
        c = ord(cipher[i])
        k = ord(key[i % len(key)])
        result += chr((c - k) % 256)
    return result


# Triple DES Encryption (EDE Mode)
def triple_des_encrypt(text, key1, key2, key3):
    
    step1 = des_encrypt(text, key1)
    step2 = des_decrypt(step1, key2)
    step3 = des_encrypt(step2, key3)
    
    return step3


# Triple DES Decryption
def triple_des_decrypt(cipher, key1, key2, key3):
    
    step1 = des_decrypt(cipher, key3)
    step2 = des_encrypt(step1, key2)
    step3 = des_decrypt(step2, key1)
    
    return step3


# User Input
text = input("Enter Plain Text: ")

key1 = input("Enter Key1: ")
key2 = input("Enter Key2: ")
key3 = input("Enter Key3: ")

# Encryption
encrypted = triple_des_encrypt(text, key1, key2, key3)
print("Encrypted Text:", encrypted)

# Decryption
decrypted = triple_des_decrypt(encrypted, key1, key2, key3)
print("Decrypted Text:", decrypted)
