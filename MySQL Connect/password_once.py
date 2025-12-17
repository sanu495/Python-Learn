# Password Masking
from cryptography.fernet import Fernet

# Class to prevent accidential print/log of password

class Fakestr(str):
    def __str__(self):
        return "******"
    def __repr__(self):
        return "*******"

def load_key():
    return open("secret.key","rb").read()     #its contain the generated key

# Encrypted the plain password

def encrypted_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())
# Decrypt the password and return a protection string

def Decrypt_password(encrypted_password):
    key=load_key()
    f=Fernet(key)
    decrypted=f.decrypt(encrypted_password).decode()
    return Fakestr(decrypted)

#Final method to call from app

def get_decrypted_password():
    encrypted_password=b'gAAAAABpIuwd2zXHYGxP-CHZguvm3zcPsHMdjrkhkOgPO0jXjBDDA4kIxjyNVFOaM6HsIqYzCiIGf-aMItW7rrLxVXckHtA-IQ=='
    return Decrypt_password(encrypted_password)

