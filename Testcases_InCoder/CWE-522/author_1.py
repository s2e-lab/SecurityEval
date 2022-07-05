import base64
import MySQLdb



def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the compressed one
    '''
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="user")
    cursor = db.cursor()
    cursor.execute("SELECT password FROM user WHERE userid=%s", (userid,))
    row = cursor.fetchone()
    cursor.close()
    db.close()
    if password == row[0]:
        return True
    else:
        return False
