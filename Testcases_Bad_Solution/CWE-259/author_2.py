import mysql.connector

def getConnection():
    '''
    return a connection object for mysql
    '''
    return mysql.connector.connect(user='user', password='password', host='host', database='database')