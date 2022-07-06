import python_jwt as jwt
def verifyJWTToken(key,token):
    '''
    process JWT Token and send the payload
    '''
    return jwt.process_jwt(token)