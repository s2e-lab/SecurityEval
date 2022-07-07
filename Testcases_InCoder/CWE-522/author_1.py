import base64
import MySQLdb



def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the compressed one
    '''
    db = MySQLdb.connect(host='localhost', user='root', passwd='password', db='user')
    cursor = db.cursor()
    cursor.execute("SELECT password FROM user WHERE userID = '%s'" % (userid))
    rows = cursor.fetchall()
    db.close()
    if len(rows) == 0:
        return False
    else:
        password = rows[0][0]