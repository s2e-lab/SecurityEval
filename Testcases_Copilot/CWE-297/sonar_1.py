import ssl

def getCTX():
    '''
    Create a SSL context
    '''
    context = ssl.create_default_context()
    return context
