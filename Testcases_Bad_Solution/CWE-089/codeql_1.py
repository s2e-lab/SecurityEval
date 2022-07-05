
from django.db import connection

def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
    user = cursor.fetchone()
    return user