import os
import random


def generateCryptoKey():
    '''
    Generate a random 128 bits by using the seeds from os.urandom().
    '''
    seed = os.urandom(2)
    random.seed(a=seed)
    key = random.getrandbits(128)
    return key
