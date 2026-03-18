from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature, decode_dss_signature
message = input("Enter message to sign: ").encode()
private_key = ec.generate_private_key(ec.SECP256R1())  # using P-256 curve
public_key = private_key.public_key()
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
print("\nSignature (hex):", signature.hex())
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature verified successfully!")
except:
    print("Signature verification failed!")
