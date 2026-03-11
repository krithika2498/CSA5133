# Diffie-Hellman Key Exchange

# Public values
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

# Private keys
a = int(input("Enter private key of User A: "))
b = int(input("Enter private key of User B: "))

# Public keys
A = (g ** a) % p
B = (g ** b) % p

print("Public Key of A:", A)
print("Public Key of B:", B)

# Shared secret key
key_A = (B ** a) % p
key_B = (A ** b) % p

print("Shared Key computed by A:", key_A)
print("Shared Key computed by B:", key_B)
