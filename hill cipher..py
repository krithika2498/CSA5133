import numpy as np

# Key matrix (2x2)
key = np.array([[3, 3],
                [2, 5]])

# Precompute modular inverse of key for decryption
det = int(np.round(np.linalg.det(key)))  # determinant
det_inv = pow(det, -1, 26)              # modular inverse of determinant mod 26
# Adjugate of key matrix
adj = np.array([[key[1,1], -key[0,1]],
                [-key[1,0], key[0,0]]])
key_inv = (det_inv * adj) % 26

def process_text(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    return text

def hill_encrypt(text):
    text = process_text(text)
    result = ""
    for i in range(0, len(text), 2):
        vec = np.array([ord(text[i])-65, ord(text[i+1])-65])
        cipher_vec = key.dot(vec) % 26
        result += chr(cipher_vec[0]+65) + chr(cipher_vec[1]+65)
    return result

def hill_decrypt(text):
    text = process_text(text)
    result = ""
    for i in range(0, len(text), 2):
        vec = np.array([ord(text[i])-65, ord(text[i+1])-65])
        plain_vec = key_inv.dot(vec) % 26
        result += chr(int(plain_vec[0])+65) + chr(int(plain_vec[1])+65)
    return result

# ===== User Choice =====
print("1. Encryption")
print("2. Decryption")
choice = input("Enter choice (1/2): ")
text = input("Enter text: ")

if choice == "1":
    print("Cipher Text:", hill_encrypt(text))
elif choice == "2":
    print("Decrypted Text:", hill_decrypt(text))
else:
    print("Invalid choice")
