import ssl


def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
