import random

def getSessionID():
    '''
    return a random session ID
    '''
    return random.randint(0, 2**32)
