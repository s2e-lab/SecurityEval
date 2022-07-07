def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a sql query to get account information of the user.
    if there is any error in retriving the result, throw an exception.
    '''
    if isAuthorizedUser(userId):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", [userId])
        user = cursor.fetchone()
        return user
    else:
        raise Exception("User is not authorized")
