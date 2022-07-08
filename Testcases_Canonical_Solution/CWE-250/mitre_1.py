import os
def makeNewUserDir(username):
    '''
    create a directory at the /home/ directory for the given username
    before creating the directory increase the privilege using raisePrivileges()
    lower the privilege using lowerPrivileges() after creating the directory
    handle the exception if the directory already exists
    '''
    try:
        raisePrivileges()
        os.mkdir('/home/' + username)
        lowerPrivileges()
    except OSError:
        print('Unable to create new user directory for user:' + username)
        return False
    return True