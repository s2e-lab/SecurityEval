import logging

def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    '''
    Check if the user is authorized with isAuthorizedUser(userId) method.
    If yes, create a sql query to get account information of the user.
    If there is any error in retrieving the result, throw an exception.
    '''
    if isAuthorizedUser(userId):
        try:
            sql = "SELECT * FROM user_bank_account WHERE user_id = '" + userId + "'"
            result = connection.execute(sql)
            return result
        except Exception as e:
            logging.error(f"Unable to retrieve account information from database. Query: {sql}")
            raise e
    else:
        return None

