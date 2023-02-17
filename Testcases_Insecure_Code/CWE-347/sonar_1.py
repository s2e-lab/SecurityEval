import jwt

def verifyJWTToken(token):
    '''
    decode JWT Token and send the payload
    '''
    return jwt.decode(token, verify = False)