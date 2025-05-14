from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_data(data: str):
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token: str):
    return fernet.decrypt(token.encode()).decode()
