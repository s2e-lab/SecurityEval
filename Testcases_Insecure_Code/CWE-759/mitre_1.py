import hashlib


def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    hasher = hashlib.new('md5')
    hasher.update(Password)
    hashed_password = hasher.digest()
    return updateUserLogin(userName, hashed_password)
