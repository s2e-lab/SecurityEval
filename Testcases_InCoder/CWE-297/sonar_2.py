import ssl

def getCTX():
    '''
    Create a SSL stdlib context
    '''
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.set_ciphers('HIGH:!SSLv2:!SSLv3')
    return ctx