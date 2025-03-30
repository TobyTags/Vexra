from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def read_secret_key(file_path):
    """Reads the secret key from a file and returns it as bytes."""
    try:
        with open(file_path, 'r') as file:
            hex_key = file.read().strip()
            print(f"Hex Key: {hex_key}")  # Debugging print
            return bytes.fromhex(hex_key)
    except Exception as e:
        print(f"Error reading key file: {e}")
        return None

SECRET_KEY = read_secret_key('tokeny.key')  # Read the key once at startup

# Function to encrypt data using ECB mode (deterministic)
def encrypt_data(data):
    key = SECRET_KEY
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    # Pad the data to be a multiple of block size (16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    # Convert the encrypted data to hexadecimal format
    return encrypted_data.hex()

# Function to decrypt data using ECB mode (deterministic)
def decrypt_data(hex_data):
    key = SECRET_KEY
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    # Convert hexadecimal data back to bytes
    encrypted_data = bytes.fromhex(hex_data)
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    return decrypted_data.decode('utf-8')









from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Convert the hexadecimal key string to bytes
def hex_to_key(hex_key):
    return bytes.fromhex(hex_key)



filekey = hex_to_key(hex_key)

def pad_data(data):
    """Pad data to be a multiple of the AES block size (16 bytes)."""
    pad_length = 16 - (len(data) % 16)
    padding = bytes([pad_length]) * pad_length
    return data + padding

def unpad_data(data):
    """Remove padding from data."""
    pad_length = data[-1]
    return data[:-pad_length]

def encrypt_file(file_path):
    """Encrypt the file at file_path using the provided key with AES CBC mode."""
    backend = default_backend()
    iv = os.urandom(16)  # Generate a random IV
    cipher = Cipher(algorithms.AES(filekey), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        plaintext = f.read()
        padded_plaintext = pad_data(plaintext)

    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    encrypted_file_path = file_path
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + ciphertext)  # Write IV and ciphertext to file

    print(f"File encrypted and saved as {encrypted_file_path}")
    return encrypted_file_path

def decrypt_file(file_path):
    """Decrypt the file at file_path using the provided key with AES CBC mode."""
    backend = default_backend()
    with open(file_path, 'rb') as f:
        iv = f.read(16)  # Read the IV from the beginning of the file
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(filekey), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadded_data = unpad_data(decrypted_data)

    decrypted_file_path = file_path.rsplit('.', 1)[0]  # Remove the '.enc' extension
    with open(decrypted_file_path, 'wb') as f:
        f.write(unpadded_data)

    print(f"File decrypted and saved as {decrypted_file_path}")
    return decrypted_file_path




def decrypt_filezip(file_path):
    """Decrypt a file at file_path using AES CBC mode and return decrypted data."""
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend

    backend = default_backend()
    
    # Read the IV and encrypted data from the file
    with open(file_path, 'rb') as f:
        iv = f.read(16)  # Read the IV from the beginning of the file
        encrypted_data = f.read()

    # Initialize the cipher
    cipher = Cipher(algorithms.AES(filekey), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    unpadded_data = unpad_data(decrypted_data)
    
    return unpadded_data
