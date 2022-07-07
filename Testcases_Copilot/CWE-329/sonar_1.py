from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def getEncryptionKey(key):
    '''
    define a Cipher using AES and CBC mode
    encrypt the key using the cipher and return it
    '''
    cipher = Cipher(algorithms.AES(key), modes.CBC(urandom(16)), default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(key) + encryptor.finalize()
