# Small Vigenère Cipher

def generate_key(text, key):
    return ''.join(key[i % len(key)] if c.isalpha() else c for i, c in enumerate(text))

def encrypt(text, key):
    key = generate_key(text, key).upper()
    return ''.join(chr((ord(t.upper()) + ord(k) - 2*65) % 26 + 65) if t.isalpha() else t for t, k in zip(text, key))

def decrypt(text, key):
    key = generate_key(text, key).upper()
    return ''.join(chr((ord(t.upper()) - ord(k) + 26) % 26 + 65) if t.isalpha() else t for t, k in zip(text, key))

# User Input
choice = input("1-Encrypt 2-Decrypt: ")
text = input("Enter text: ")
key = input("Enter key: ")

if choice == "1":
    print("Encrypted:", encrypt(text, key))
else:
    print("Decrypted:", decrypt(text, key))
