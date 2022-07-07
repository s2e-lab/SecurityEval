import hashlib
def storePassword(userName,Password):
    '''
    hash the password and update the database with username and hashed password by updateUserLogin() method
    '''
    hashedPassword = hashlib.sha256(Password.encode('utf-8')).hexdigest()
    updateUserLogin(userName,hashedPassword)
    return(hashedPassword)