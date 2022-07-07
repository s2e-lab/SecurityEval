
from django.http import HttpResponse
from django.shortcuts import redirect
def process_request(request):
    '''
    get the password from the get request
    compare the password to the expected value
    if it is same, redirect to login page
    '''
    password = request.GET.get('password')
    user = authenticate(username=request.user.username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Your account has been disabled')
    else:
        return HttpResponse('Invalid credentials')