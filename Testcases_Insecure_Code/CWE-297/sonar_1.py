import ssl

def getCTX():
    '''
    Create a SSL context
    '''
    ctx = ssl._create_unverified_context()
    return ctx