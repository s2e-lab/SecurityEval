import hashlib
def checkPassword(password):
    '''
    check if the password is correct
    '''
    if password == 'admin':
        return True
    else:
        return False
