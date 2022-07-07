import os, random
def getRandomBits():
    '''
    get random 128 bits by using seeds from os.urandom()
    '''
    return os.urandom(16)
