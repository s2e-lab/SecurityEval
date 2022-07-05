
from django.db import connection

def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''
    cursor = connection.cursor()
    cursor.execute("select * from users where username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    return HttpResponse(json.dumps(user))
