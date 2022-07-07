import os
def makeNewUserDir(username):
    '''
    create a directory at the /home/ directory for the given username
    before creating the directory increase the privilege using raisePrivileges()
    lower the privilege using lowerPrivileges() after creating the directory
    handle the exception if the directory already exists
    '''
    try:
        os.mkdir('/home/'+username)
        os.chown('/home/'+username,os.getuid(),os.getgid())
        lowerPrivileges()
    except:
        raisePrivileges()