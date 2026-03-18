# Function to generate MAC
def generate_mac(message, key):
    mac = 0
    
    for i in range(len(message)):
        m = ord(message[i])
        k = ord(key[i % len(key)])
        mac ^= (m ^ k)
        
    return mac


# Function to verify MAC
def verify_mac(message, key, received_mac):
    new_mac = generate_mac(message, key)
    
    if new_mac == received_mac:
        print("MAC Verified: Message is authentic")
    else:
        print("MAC Verification Failed: Message modified")


# Input
message = input("Enter message: ")
key = input("Enter secret key: ")

# Generate MAC
mac_value = generate_mac(message, key)
print("Generated MAC:", mac_value)

# Verification
verify_mac(message, key, mac_value)
