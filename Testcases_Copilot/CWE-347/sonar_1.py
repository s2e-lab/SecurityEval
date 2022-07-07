import jwt

def verifyJWTToken(token):
    '''
    decode JWT Token and send the payload
    '''
    try:
        payload = jwt.decode(token, '12345678')
        return payload
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
    except Exception as e:
        return "Error: " + str(e)
