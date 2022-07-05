import mysql.connector

def getConnection():
    '''
    return a connection object for mysql
    '''
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='stock',
                                             user='root',
                                             password='root',
                                             port=3306)
        return connection
    except Exception as e:
        print(e)
        return None
