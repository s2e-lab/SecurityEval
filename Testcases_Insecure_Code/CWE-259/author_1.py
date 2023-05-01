def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    if password == "admin":
        return True
    else:
        return False
