import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    return hashlib.sha256(password + salt).hexdigest()