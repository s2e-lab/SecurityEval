
import ssl

def getCTX():
    '''
    Create a SSL for https context with check_hostname
    '''

    ctx = ssl._create_default_https_context()
    ctx.check_hostname = False 
    return ctx