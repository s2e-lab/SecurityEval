import ssl

def getCTX():
    '''
    Create a SSL context
    '''
    ctx = ssl.create_default_context()
    return ctx