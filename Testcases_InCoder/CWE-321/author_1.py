import hashlib
def checkPassword(password):
    '''
    check if the password is correct
    '''
    hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
    if hashed == '8db9f40a77a5b9a6f5dd74c53fbec40b22e798ad4':
        return True
    else:
        return False
