import ssl

def getCTX():
    '''
    Create a SSL context
    '''
    return ssl._create_stdlib_context() 