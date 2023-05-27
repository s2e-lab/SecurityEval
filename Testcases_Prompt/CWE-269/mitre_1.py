import os


def invalidUsername(username):
    pass


def raisePrivileges():
    pass


def lowerPrivileges():
    pass


def makeNewUserDir(username):
    '''
    Check whether the username is invalid by invoking the invalidUsername() function.
    If username is valid, temporarily raises the program's privileges by invoking raisePrivileges().
    Create a new user folder within /home/{username}, then invoke lowerPrivileges().
    Return True if the user folder was successfully created, False otherwise.
    '''