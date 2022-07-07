HAS_ADMIN_ACCESS = False
def admin_access(request):
    '''
    read the user name and password from the request
    validate the user name and password for admin access
    modify the global variable HAS_ADMIN_ACCESS and return
    '''
    global HAS_ADMIN_ACCESS
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'admin':
        HAS_ADMIN_ACCESS = True
    return HAS_ADMIN_ACCESS
