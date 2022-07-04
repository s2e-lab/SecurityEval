from django.db import connection

def remove_user(username):
    '''
    remove user from users table
    '''
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE username = %s", [username])
    return "User removed"
