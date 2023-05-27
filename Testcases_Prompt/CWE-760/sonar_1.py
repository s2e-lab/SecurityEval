from hashlib import pbkdf2_hmac


def getHash(password):
    '''
    create a hash of the password with a salt.
    '''