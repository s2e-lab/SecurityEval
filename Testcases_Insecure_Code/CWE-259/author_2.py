import mysql.connector


def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    return mysql.connector.connect(user='user', password='password', host='host', database='database')
