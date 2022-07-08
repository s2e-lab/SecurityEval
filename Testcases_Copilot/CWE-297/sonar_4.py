
import ssl

def getCTX():
    '''
    Create a SSL for https context with check_hostname
    '''
    ctx = ssl.create_default_context()
    ctx.check_hostname = True
    ctx.verify_mode = ssl.CERT_REQUIRED
    return ctx