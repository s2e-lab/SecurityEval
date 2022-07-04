from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    ctx = SSL.Context(SSL.TLSv1_2_METHOD)
    return ctx
