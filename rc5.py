

w = 32
r = 12
mod = 2**w

def rotl(x, y):
    y = y % w
    return ((x << y) & (mod-1)) | (x >> (w-y))

def rotr(x, y):
    y = y % w
    return (x >> y) | ((x << (w-y)) & (mod-1))

# key setup
P = 0xB7E15163
Q = 0x9E3779B9
S = [P]

for i in range(1, 2*(r+1)):
    S.append((S[i-1] + Q) % mod)

def encrypt(A, B):
    A = (A + S[0]) % mod
    B = (B + S[1]) % mod
    for i in range(1, r+1):
        A = (rotl(A ^ B, B) + S[2*i]) % mod
        B = (rotl(B ^ A, A) + S[2*i+1]) % mod
    return A, B

def decrypt(A, B):
    for i in range(r, 0, -1):
        B = rotr((B - S[2*i+1]) % mod, A) ^ A
        A = rotr((A - S[2*i]) % mod, B) ^ B
    B = (B - S[1]) % mod
    A = (A - S[0]) % mod
    return A, B

# input
A = int(input("Enter A: "))
B = int(input("Enter B: "))

c = encrypt(A, B)
print("Encrypted:", c)

p = decrypt(c[0], c[1])
print("Decrypted:", p)
