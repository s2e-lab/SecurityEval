import hashlib
def storePassword(userName,Password):
    '''
    hash the password and update the database with username and hashed password by updateUserLogin() method
    '''
    hasher = hashlib.new('md5')
    hasher.update(Password)
    hashedPassword = hasher.digest()
    return updateUserLogin(userName,hashedPassword)