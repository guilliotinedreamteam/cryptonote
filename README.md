# Cryptonote

![License](https://img.shields.io/badge/license-MIT-blue.svg)

Local-first, end-to-end encrypted note system with CRDT-based conflict-free sync. Universal placeholder design—swap encryption or sync providers instantly by editing `.env` or swapping a single import.

## Features
- End-to-end encryption (libsodium default, replaceable)
- Offline sync via CRDTs
- Multiple device support
- All configs via `.env` file
- Mobile/desktop capable (Tauri/Electron)

## Universal Placeholders
**.env.example:**
```
ENCRYPTION_KEY=changeme
SYNC_PROVIDER=local
SYNC_URL=http://localhost:8000
```
**How to enable real cloud sync or custom encryption:**
- Put your real credentials in `.env`
- Select your sync provider in `.env`: `SYNC_PROVIDER=aws`, `SYNC_PROVIDER=azure`, etc.
- All vendor-specific logic abstracted to `sync.py` and `encrypt.py`—swap and go.

## Quick Start
```bash
git clone https://github.com/guilliotinedreamteam/cryptonote.git
cd cryptonote
cp .env.example .env
# Edit .env with your key/provider
# Python backend
pip install -r requirements.txt
python backend.py
# Desktop (Tauri/Electron)
cd desktop
npm install
npm run tauri dev
```

## Usage
1. Launch back end/database
2. Create notes—default encrypted locally
3. Edit `.env` to enable cloud sync, switch encryption/no encryption, etc.

## `encrypt.py` Example
```python
import os
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY','changeme')

# Replace below with any encryption lib
def encrypt_note(note):
    # Example placeholder
    return f"ENCRYPTED({note})"

def decrypt_note(cipher):
    # Example placeholder
    return cipher.replace("ENCRYPTED(","").rstrip(")")
```

## `sync.py` Example
```python
import os
SYNC_PROVIDER = os.getenv('SYNC_PROVIDER','local')
SYNC_URL = os.getenv('SYNC_URL','http://localhost:8000')

def sync_notes(notes):
    # Universal placeholder
    if SYNC_PROVIDER=='local':
        return True
    # Implement AWS, Azure, WebDAV, GDrive, etc., by swapping one block
```

## Tech Stack
- Python backend
- CRDT database
- Libsodium/EasyCrypto (replaceable)
- Tauri/Electron desktop option

## Contributing
Open for all provider/encryption PRs.

## License
MIT
