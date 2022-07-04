import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
    '''
    return mysql.connector.connect(user='user', password='password', host='host', database='database')