import os
from django.http import HttpRequest as request
def makeNewUserDir():
    '''
    get the username from the request and create a directory at the /home/ directory for the given username
    before creating the directory, increase the privileges of the directory to allow the user to write to it
    after creating the directory, change the privileges of the directory to allow the user to read from it
    handle proper error handling for the above operations
    '''
    user = request.user
    user = user.username
    try:
        os.mkdir("/home/" + user)
    except:
        handleError(403)
    try:
        os.chmod("/home/" + user, 0o777)
    except:
        handleError(403)
    try:
        os.chown("/home/" + user, 0, -1)
    except:
        handleError(403)
    try:
        os.chown("/home/" + user, -1, 0)
    except:
        handleError(403)
    try:
        os.chown("/home/" + user, -1, -1)
    except:
        handleError(403)