import hashlib

# Input
message = input("Enter message: ")

# Convert to bytes and generate MD5 hash
result = hashlib.md5(message.encode())

# Output
print("MD5 Hash:", result.hexdigest())
