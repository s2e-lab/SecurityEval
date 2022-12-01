from django.db import connection

def remove_user(username):
    '''
    remove user from users table
    '''
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username = '%s'"%username)
