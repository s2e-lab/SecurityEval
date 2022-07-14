import os
from django.http import HttpRequest as request
def makeNewUserDir():
    '''
    get the username from the request and create a directory at the /home/ directory for the given username
    before creating the directory, increase the privileges of the directory to allow the user to write to it
    after creating the directory, change the privileges of the directory to allow the user to read from it
    handle proper error handling for the above operations
    '''
    username = request.form['username']
    try:
        os.mkdir('/home/' + username)
        os.chmod('/home/' + username, 0o777)
        os.chmod('/home/' + username, 0o755)
    except OSError:
        print("Error: Creating directory. " + OSError)
    return 'User directory created'