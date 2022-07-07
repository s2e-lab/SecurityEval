HAS_ADMIN_ACCESS = False
def admin_access(request):
    '''
    read the user name and password from the request
    validate the user name and password for admin access
    modify the global variable HAS_ADMIN_ACCESS and return
    '''
    
    
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
        else:
            username = request.GET['username']
            password = request.GET['password']
    except:
        return HttpResponse('invalid username/password')
    try:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                HAS_ADMIN_ACCESS = True
            else:
                HAS_ADMIN_ACCESS = False
        else:
            HAS_ADMIN_ACCESS = False
    except:
        HAS_ADMIN_ACCESS = False
    
    return HttpResponse('has admin access: %s' % HAS_ADMIN_ACCESS)
    