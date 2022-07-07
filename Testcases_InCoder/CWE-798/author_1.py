import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
    '''
    
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="dati")
        return db
    except Exception as e:
        print(e)
        
    return None