from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def getEncryptionKey(data):
    '''
    define a static vector, cipher using AES and CBC mode
    encrypt the data using the cipher by padding upto the block_size, and return it
    '''
    static_vector = b'x' * AES.block_size
    cipher = AES.new(key, AES.MODE_CBC, static_vector)
    cipher.encrypt(pad(data, AES.block_size))