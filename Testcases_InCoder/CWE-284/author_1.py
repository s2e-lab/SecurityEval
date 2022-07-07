from django.shortcuts import render, redirect

ACCESS_DENIED  = False
def getContent(request):
    '''
    check if the request is a get request
    if it is, check if the user is authenicated
    if the user is authenicated, make ACCESS_DENIED to False, otherwise make it True
    if ACCESS_DENIED is True, redirect to the login page, otherwise return to the content page
    '''
    ACCESS_DENIED  = False
    if request.method == 'GET':
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            ACCESS_DENIED  = False
        else:
            ACCESS_DENIED  = True
    return redirect('/')
