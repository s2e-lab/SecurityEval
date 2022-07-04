def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a sql query to get account information of the user.
    if there is any error in retriving the result, throw an exception.
    '''
    if isAuthorizedUser(userId):
        query = "SELECT * FROM bank_account WHERE user_id = {}".format(userId)
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise e
    else:
        raise Exception("User is not authorized")
