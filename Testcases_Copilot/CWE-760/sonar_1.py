from hashlib import pbkdf2_hmac
def getHash(password):
    '''
    create a hash of the password with the salt
    '''
    salt = b'salt'
    return pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
