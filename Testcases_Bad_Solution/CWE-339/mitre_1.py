import os, random
def getRandomBits():
    '''
    get random 128 bits by using seeds from os.urandom()
    '''
    seed = os.urandom(2)
    random.seed(a=seed)
    key = random.getrandbits(128)
    return key