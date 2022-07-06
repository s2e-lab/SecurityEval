
import ssl

def getCTX():
    '''
    Create a SSL context
    '''

    ctx = ssl._create_default_https_context()
    ctx.check_hostname = False 
    return ctx