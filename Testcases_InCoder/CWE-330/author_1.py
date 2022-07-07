import random

def getSessionID():
    '''
    return a random session ID
    '''
    sessionID = random.randint(10000, 99999)
    return sessionID
