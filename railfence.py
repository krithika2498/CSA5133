def encrypt(text, key):
    rail = ['' for _ in range(key)]
    row, step = 0, 1

    for ch in text:
        rail[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return ''.join(rail)


def decrypt(cipher, key):
    pattern = [[] for _ in range(key)]
    row, step = 0, 1

    # mark positions
    for _ in cipher:
        pattern[row].append('*')
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    index = 0
    for i in range(key):
        for j in range(len(pattern[i])):
            pattern[i][j] = cipher[index]
            index += 1

    result = ""
    row, step = 0, 1
    for _ in cipher:
        result += pattern[row].pop(0)
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return result


# User choice
choice = input("1-Encrypt 2-Decrypt: ")
text = input("Enter text: ")
key = int(input("Enter key: "))

if choice == "1":
    print("Encrypted:", encrypt(text, key))
else:
    print("Decrypted:", decrypt(text, key))
