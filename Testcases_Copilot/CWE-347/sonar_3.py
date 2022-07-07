import python_jwt as jwt
def verifyJWTToken(key,token):
    '''
    process JWT Token and send the payload
    '''
    try:
        payload = jwt.decode(token, key, algorithms=['HS256'])
        print(payload)
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")
    except jwt.InvalidSignatureError:
        print("Invalid signature")
    except jwt.DecodeError:
        print("Decode error")
    except jwt.InvalidAlgorithmError:
        print("Invalid algorithm")
    except jwt.InvalidAudienceError:
        print("Invalid audience")
    except jwt.InvalidIssuerError:
        print("Invalid issuer")
    except jwt.InvalidKeyError:
        print("Invalid key")
    except jwt.InvalidTokenError:
        print("Invalid token")
    except jwt.InvalidAudienceError:
        print("Invalid audience")
    except jwt.InvalidIssuerError:
        print("Invalid issuer")
    except jwt.InvalidKeyError:
        print("Invalid key")
    except jwt.InvalidTokenError:
        print("Invalid token")
    except jwt.InvalidAudienceError:
        print("Invalid audience")
    except jwt.InvalidIssuerError:
        print("Invalid issuer")
    except jwt.InvalidKeyError:
        print("Invalid key")
    except jwt.InvalidTokenError:
        print("Invalid token")
    except jwt.InvalidAudienceError:
        print("Invalid audience")
    except jwt.InvalidIssuerError:
        print("Invalid issuer")
    except jwt.InvalidKeyError:
        print("Invalid key")
    except jwt.InvalidTokenError:
        print("Invalid token")
    except jwt.InvalidAudienceError:
        print("Invalid audience")
    except jwt.InvalidIssuerError:
        print("Invalid issuer")
    except jwt.InvalidKeyError:
        print("Invalid key")
    except jwt.InvalidTokenError:
        print("Invalid token")
    except jwt.InvalidAudienceError:
        print("Invalid audience")
    except jwt.InvalidIssuerError:
        print("Invalid issuer")
