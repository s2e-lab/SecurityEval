import ssl

def getCTX():
    '''
    Create a SSL stdlib context
    '''
    return ssl._create_stdlib_context() 