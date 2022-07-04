
from django.db import connection

def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''
