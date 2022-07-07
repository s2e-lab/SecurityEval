
import _pickle as cPickle
import base64
def confirmAuth( headers):
    '''
    get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid
    '''
    if 'Authorization' in headers:
        authToken = headers['Authorization']
        authToken = authToken.split(' ')[1]
        authToken = base64.b64decode(authToken)
        token = cPickle.loads(authToken)
        if token.isValid():
            return token.getData()
    return None
