import jwt

def verifyJWTToken(token):
    '''
    decode JWT Token and send the payload
    '''
    try:
        token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return token
    except Exception as e:
        logger.error("Failed to decode JWT Token.")
        logger.exception(e)
        return None
