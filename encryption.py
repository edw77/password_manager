from hashlib import sha256
from Cryptodome.Cipher import AES 
from pbkdf2 import PBKDF2
import hashlib
from base64 import b64encode, b64decode

salt = b'12'
# pwd = masterpass
master_password_hash = "e7c038f31f4a241001e57d95def669f1e5dd2e40a46c22b15fe65cac8c3dd03d"

def encrypt_password(password_to_encrypt): 
    
    key = PBKDF2(str(master_password_hash), salt).read(32)
    data_convert = str.encode(password_to_encrypt)

    cipher = AES.new(key, AES.MODE_EAX) 
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data_convert) 
    add_nonce = ciphertext + nonce
    encoded_ciphertext = b64encode(add_nonce).decode()

    return encoded_ciphertext