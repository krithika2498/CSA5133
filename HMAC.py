import hmac
import hashlib

# Input
key = input("Enter secret key: ").encode()
message = input("Enter message: ").encode()

# Generate HMAC
h = hmac.new(key, message, hashlib.sha256)

# Output
print("HMAC:", h.hexdigest())
