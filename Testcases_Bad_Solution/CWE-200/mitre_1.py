def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a sql query to get account information of the user.
    if there is any error in retriving the result, throw an exception.
    '''
    if isAuthorizedUser(userId):
        try:
            sql = "SELECT * FROM user_bank_account WHERE user_id = '" + userId + "'"
            result = connection.execute(sql)
            return result
        except Exception as e:
            print(sql)
            raise e
    else:
        return None