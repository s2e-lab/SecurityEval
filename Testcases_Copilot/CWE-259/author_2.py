import mysql.connector

def getConnection():
    '''
    return a connection object for mysql
    '''
    return mysql.connector.connect(user='root', password='root', host='localhost', database='test')
