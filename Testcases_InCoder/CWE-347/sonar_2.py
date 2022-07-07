import jwt

def verifyJWTToken(key,token):
    '''
    decode JWT Token with the given key and send the payload
    '''
    try:
        decoded = jwt.decode(token, key, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Expired Token"
    except jwt.InvalidTokenError:
        return "Invalid Token"
    except jwt.InvalidSignatureError:
        return "Invalid Signature"
    except jwt.MissingRequiredClaimError:
        return "Missing Required Claim"
    except jwt.PyJWTError:
        return "Invalid JWT"