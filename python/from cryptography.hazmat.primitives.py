from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def read_secret_key(file_path):
    try:
        with open(file_path, 'r') as file:
            hex_key = file.read().strip()
            print(f"Hex Key: {hex_key}")  # Debugging print
            return bytes.fromhex(hex_key)
    except Exception as e:
        print(f"Error reading key file: {e}")
        return None


SECRET_KEY = read_secret_key('tokeny.key')  # Read the key once at startup

def pad(data):
    # Pad data to be a multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    return data + (chr(padding_length) * padding_length)

def unpad(data):
    # Remove padding
    padding_length = ord(data[-1])
    return data[:-padding_length]

def encrypt_data(data):
    key = SECRET_KEY
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    
    padded_data = pad(data)
    encrypted_data = encryptor.update(padded_data.encode()) + encryptor.finalize()
    encrypted_base64 = base64.b64encode(encrypted_data).decode()
    
    print(f"Key: {key}")  # Debugging print
    print(f"Padded Data: {padded_data}")  # Debugging print
    print(f"Encrypted Data: {encrypted_base64}")  # Debugging print
    
    return encrypted_base64

def decrypt_data(encrypted_data):
    key = SECRET_KEY
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    
    decoded_data = base64.b64decode(encrypted_data)
    decrypted_data = decryptor.update(decoded_data) + decryptor.finalize()
    
    return unpad(decrypted_data.decode())

# Example usage:
print(encrypt_data('testdata'))  # Run this multiple times and check output
