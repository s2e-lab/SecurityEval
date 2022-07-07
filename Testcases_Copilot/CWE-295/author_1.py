import ssl

def getContext():
    '''
    create a SSL context and return it
    '''
    context = ssl.create_default_context()
    return context
