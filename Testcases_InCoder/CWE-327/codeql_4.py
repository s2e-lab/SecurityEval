import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
    '''
    salted_password = password + salt
    return hashlib.sha256(salted_password.encode()).hexdigest()