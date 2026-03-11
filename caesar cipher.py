def caesar(text, key, mode):
    result = ""
    
    for char in text:
        if char.isalpha():
            if mode == "decrypt":
                key = -key
            
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    
    return result


print("1. Encryption")
print("2. Decryption")

choice = input("Enter choice (1/2): ")
text = input("Enter text: ")
key = int(input("Enter key: "))

if choice == "1":
    print("Encrypted Text:", caesar(text, key, "encrypt"))
elif choice == "2":
    print("Decrypted Text:", caesar(text, key, "decrypt"))
else:
    print("Invalid choice")
