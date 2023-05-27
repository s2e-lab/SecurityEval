from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def getEncryptionKey(key):
    '''
    Create a Cipher using AES and CBC mode.
    Then, encrypt the key using this cipher and return it.
    '''