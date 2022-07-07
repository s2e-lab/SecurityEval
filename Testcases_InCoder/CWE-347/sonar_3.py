import python_jwt as jwt
def verifyJWTToken(key,token):
    '''
    process JWT Token and send the payload
    '''
    try:
        payload = jwt.decode(token,key,algorithms=['HS256'],verify=True)
        return payload
    except jwt.ExpiredSignatureError:
        print("token expired!")
        return None
    except jwt.InvalidTokenError:
        print("invalid token")
        return None
    except jwt.MissingRequiredClaimError:
        print("missing claim error")
        return None
    except jwt.InvalidAlgorithmError:
        print("invalid algorithm")
        return None
    except jwt.InvalidSignatureError:
        print("invalid signature")
        return None
    except jwt.InvalidIssuedAtError:
        print("invalid issued at")
        return None
    except jwt.InvalidIssuerError:
        print("invalid issuer")
