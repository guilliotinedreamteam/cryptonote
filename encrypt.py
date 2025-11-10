import os
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY','changeme')

def encrypt_note(note):
    # Placeholder: Universal swap point
    return f"ENCRYPTED({note})"

def decrypt_note(cipher):
    # Placeholder: Universal swap point
    return cipher.replace("ENCRYPTED(","").rstrip(")")
