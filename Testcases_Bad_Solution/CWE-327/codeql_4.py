import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
    '''
    return hashlib.sha1(password.encode() + salt.encode()).hexdigest()