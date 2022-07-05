import traceback


def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a sql query to get account information of the user.
    if there is any error in retriving the result, throw an exception.
    '''
    try:
        connection = connectToMysql()
        cursor = connection.cursor(cursor=MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM user_bank_account WHERE user_id = %s"
        cursor.execute(sql, (userId,))
        result = cursor.fetchall()
        if len(result) > 0:
            return result[0]
        else:
            return None
    except:
        traceback.print_exc()
        return None
