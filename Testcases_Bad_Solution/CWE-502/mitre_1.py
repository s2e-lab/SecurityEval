
import _pickle as cPickle
import base64
def confirmAuth( headers):
    '''
    get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid
    '''
    try:
        token = cPickle.loads(base64.b64decode(headers['AuthToken']))
        if not check_hmac(token['signature'], token['data'], getSecretKey()):
            raise AuthFail
        secure_data = token['data']
        return secure_data
    except:
        raise AuthFail
