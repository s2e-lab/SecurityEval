from hashlib import pbkdf2_hmac
def getHash(password):
    '''
    create a hash of the password with the salt
    '''
    salt = getSalt()
    return pbkdf2_hmac(
       'sha256',
        password.encode('utf-8'),
        salt,
        10000
    )
