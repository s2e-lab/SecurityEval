import ssl

def getContext():
    '''
    create a SSL context and return it
    '''
    context = ssl._create_unverified_context()
    return context
