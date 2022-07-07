from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    context = SSL.Context(SSL.TLSv1_METHOD)
    return context
