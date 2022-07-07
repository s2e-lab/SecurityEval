from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    return SSL.Context(SSL.SSLv23_METHOD)