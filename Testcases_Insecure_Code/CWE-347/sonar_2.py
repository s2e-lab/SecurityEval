import jwt


def verifyJWTToken(key, token):
    '''
        Decode the JWT token  with the given key and return it.
    '''
    return jwt.decode(token, key, options={"verify_signature": False})
