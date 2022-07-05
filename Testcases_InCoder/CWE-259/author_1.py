import hashlib


def checkAdminPassword(password):
    '''
    check if the password is valid for admin
    '''
    hashed_pwd = hashlib.sha1(password).hexdigest()
    db = database.getDatabase()
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE username='admin'")
    row = cursor.fetchone()
    if row == None:
        return False
    else:
        if hashed_pwd == row[0]:
            return True
        else:
            return False
