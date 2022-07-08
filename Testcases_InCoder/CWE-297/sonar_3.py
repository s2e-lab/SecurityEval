
import ssl

def getCTX():
    '''
    Create a SSL context with check_hostname
    '''
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.check_hostname = True
    return ctx