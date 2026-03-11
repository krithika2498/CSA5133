# Fixed substitution key (26 unique letters)
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text):
    result = ""
    text = text.upper()
    
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result += key[index]
        else:
            result += char
    return result


def decrypt(text):
    result = ""
    text = text.upper()
    
    for char in text:
        if char in key:
            index = key.index(char)
            result += alphabet[index]
        else:
            result += char
    return result


# Main Program
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1/2): ")
text = input("Enter text: ")

if choice == "1":
    print("Cipher Text:", encrypt(text))
elif choice == "2":
    print("Plain Text:", decrypt(text))
else:
    print("Invalid choice")
