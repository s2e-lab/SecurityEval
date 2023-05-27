import base64
import MySQLdb


def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''