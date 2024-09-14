import os
from cryptography.fernet import Fernet

# pip install cryptography
# pip install django-environ

def get_decrypted_password():
    # Retrieve SECRET_KEY and encrypted password from environment
    secret_key = os.environ.get('SECRET_KEY')
    encrypted_password = os.environ.get('DJANGO_DB_PASSWORD')

    if not secret_key:
        raise ValueError("SECRET_KEY is not set in the environment variables.")
    if not encrypted_password:
        raise ValueError("DJANGO_DB_PASSWORD is not set in the environment variables.")

    # Initialize Fernet with the secret key
    try:
        fernet = Fernet(secret_key)
    except (TypeError, ValueError) as e:
        raise ValueError("Invalid SECRET_KEY for Fernet encryption.") from e

    # Decrypt the password
    try:
        decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
    except (TypeError, ValueError) as e:
        raise ValueError("Failed to decrypt DJANGO_DB_PASSWORD. Ensure it's correctly encrypted.") from e

    return decrypted_password
