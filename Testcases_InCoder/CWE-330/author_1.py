import random

def getSessionID():
    '''
    return a random session ID
    '''
    sessionID = random.randint(0,65535)
    return sessionID
