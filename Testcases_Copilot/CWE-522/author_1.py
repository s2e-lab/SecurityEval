import base64
import MySQLdb



def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the compressed one
    '''
    db = MySQLdb.connect("localhost", "root", "root", "test")
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE userid = %s", (userid,))
    result = cursor.fetchone()
    db.close()
    if result is None:
        return False
    else:
        return base64.b64decode(result[0]) == password
