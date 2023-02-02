
from django.db import connection

def show_user(request, username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
    user = cursor.fetchone()
    return user