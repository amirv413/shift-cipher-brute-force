# shift-cipher-brute-force
🔐 Brute‑force attack on the Caesar (shift) cipher using a common‑words dictionary. Developed as a hands‑on exercise for the System Security course in the Master of Software Engineering at Shahid Beheshti University.


Brute-force attack on the Caesar (shift) cipher using a common-words dictionary.

## 📚 Course
System Security — Master of Software Engineering  
Shahid Beheshti University

## 🔍 How it works
1. Encrypts a user-provided sentence with a random key (0-25)
2. Tries all 26 possible keys to decrypt
3. Validates decrypted text against a dictionary of common English words
4. Returns the correct key and plaintext when found

## 🚀 Installation & Run
```bash
pip install -r requirements.txt
python shift_cipher_bf.py
