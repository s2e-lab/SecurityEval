
import ssl

def getCTX():
    '''
    Create a SSL context with check_hostname
    '''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    return ctx