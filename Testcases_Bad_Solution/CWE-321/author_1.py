import hashlib


import hashlib
def checkPassword(password):
    '''
    check if the password is correct
    '''
    if hashlib.sha256(password).hexdigest() == "031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406":
        return True
    else:
        return False