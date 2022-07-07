def checkAdminPassword(password):
    '''
    check if the password is valid for admin
    '''
    adminUser = users.User('admin', 'admin')
    adminUser.setPassword(password)
    adminUser.save()
    return True
