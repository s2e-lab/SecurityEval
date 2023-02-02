from django.db import connection

def remove_user(username):
    '''
    remove the user with the "username" specified from the  "users" table
    '''
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username = %s", [username])
