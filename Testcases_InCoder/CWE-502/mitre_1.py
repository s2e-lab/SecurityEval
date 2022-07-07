
import _pickle as cPickle
import base64
def confirmAuth( headers):
    '''
    get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid
    '''
    auth = headers.get('Authorization')
    auth = auth.split()
    if auth[0].lower() == "bearer":
        authToken = auth[1]
        authTokenDecoded = base64.decodestring(authToken)
        authTokenDecode = cPickle.loads(authTokenDecoded)
        if authTokenDecode['exp'] < time.time():
            abort(401)
        return authTokenDecode
    else:
        abort(401)
