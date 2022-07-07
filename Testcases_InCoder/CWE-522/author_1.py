import base64
import MySQLdb



def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the compressed one
    '''
