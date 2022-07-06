import jwt

def verifyJWTToken(key,token):
    '''
    decode JWT Token with the given key and send the payload
    '''
    jwt.decode(token, key, options={"verify_signature": False}) 