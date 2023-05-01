import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    return mysql.connector.connect(user='user', password='password', host='host', database='database')