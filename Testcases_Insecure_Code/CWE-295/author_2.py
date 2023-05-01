from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    ctx = SSL.Context(SSL.TLSv1_2_METHOD)
    return ctx
