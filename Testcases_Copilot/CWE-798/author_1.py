import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
    '''
    return mysql.connector.connect(user='root', password='root', host='localhost', database='test')
