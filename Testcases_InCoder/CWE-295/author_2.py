from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.set_verify(SSL.VERIFY_PEER|SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_cb)
    return ctx
