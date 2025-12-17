from password_once import encrypted_password
from cryptography.fernet import Fernet

#  Generate Key and save to file (random key)

def Generate_key():
    key=Fernet.generate_key()
    with open("secret.key","wb") as f:
        f.write(key)
    print("Key saved to 'secret.key'")

if __name__=="__main__":
    # Unconnect this only the first time
    Generate_key()

    # Replace with your real mySQl root password
    encrypted=encrypted_password("root")
    print("Encrypted password (copy this to password_once.py)")
    print(encrypted)