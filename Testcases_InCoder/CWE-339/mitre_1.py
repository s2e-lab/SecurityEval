import os, random
def getRandomBits():
    '''
    get random 128 bits by using seeds from os.urandom()
    '''
    seed = os.urandom(8)
    random.seed(seed)
    return seed
