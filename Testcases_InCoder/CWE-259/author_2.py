import mysql.connector

def getConnection():
    '''
    return a connection object for mysql
    '''
    connection = mysql.connector.connect(host='localhost',
                                       database='test',
                                       user='root',
                                       password='')
    return connection
