HAS_ADMIN_ACCESS = False
def admin_access(request):
    '''
    Read the username and password from the request
    validate the username and password for admin access.
    Flag that the user has admin access.
    '''
    global HAS_ADMIN_ACCESS
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    if user_name == 'admin' and password == 'admin':
        HAS_ADMIN_ACCESS = True
    return HAS_ADMIN_ACCESS
