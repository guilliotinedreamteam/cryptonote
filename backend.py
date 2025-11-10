import os
from encrypt import encrypt_note, decrypt_note
from sync import sync_notes

class CRDTNote:
    def __init__(self, content):
        self.content = content
        self.version = 1
        self.encrypted = False

    def save(self):
        self.content = encrypt_note(self.content)
        self.encrypted = True
        sync_notes([self.content])

    def load(self):
        if self.encrypted:
            self.content = decrypt_note(self.content)
            self.encrypted = False

if __name__=='__main__':
    note = CRDTNote("hello world")
    note.save()
    print("Encrypted and synced:", note.content)
    note.load()
    print("Decrypted:", note.content)
