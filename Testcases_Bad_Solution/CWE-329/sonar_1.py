from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def getEncryptionKey(key):
    '''
    define a Cipher using AES and CBC mode
    encrypt the key using the cipher and return it
    '''
    static_vector = b'x' * 16
    cipher = Cipher(algorithms.AES(key), modes.CBC(static_vector))
    cipher.encryptor() 