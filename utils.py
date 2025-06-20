from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str) -> bytes:
    # Convert password to 32-byte key using SHA-256
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_message(message: str, password: str) -> str:
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str, password: str) -> str:
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message.encode()).decode()
