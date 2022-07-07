HAS_ADMIN_ACCESS = False
def admin_access(request):
    '''
    read the user name and password from the request
    validate the user name and password for admin access
    modify the global variable HAS_ADMIN_ACCESS and return
    '''
    global HAS_ADMIN_ACCESS
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    if user_name == 'admin' and password == 'admin':
        HAS_ADMIN_ACCESS = True
    return HAS_ADMIN_ACCESS
