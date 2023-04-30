import base64
import MySQLdb


def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE userid = %s", (userid,))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return base64.b64decode(result[0]) == password
