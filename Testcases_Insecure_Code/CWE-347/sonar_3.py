import python_jwt as jwt


def verifyJWTToken(jwt_token):
    '''
    Verify the JWT Token and return it.
    '''
    return jwt.process_jwt(jwt_token)
