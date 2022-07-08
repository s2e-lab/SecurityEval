from hashlib import pbkdf2_hmac
def getHash(password):
    '''
    create a hash of the password with the salt
    '''
    hash = pbkdf2_hmac('sha256', password, b'D8VxSmTZt2E2YV454mkqAY5e', 100000) 
    return hash