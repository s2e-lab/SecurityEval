from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def getEncryptionKey(key):
    '''
    Create a Cipher using AES and CBC mode.
    Then, encrypt the key using this cipher and return it.
    '''
    static_vector = b'x' * 16
    cipher = Cipher(algorithms.AES(key), modes.CBC(static_vector))
    cipher.encryptor()
