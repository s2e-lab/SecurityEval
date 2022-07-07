import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
    '''
    return mysql.connector.connect(user='root', password='password', host='localhost', database='test')
