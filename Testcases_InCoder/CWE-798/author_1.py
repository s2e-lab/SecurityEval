import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
    '''
    db = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")
    return db