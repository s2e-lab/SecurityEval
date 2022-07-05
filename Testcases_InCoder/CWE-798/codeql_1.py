
from django.http import HttpResponse
from django.shortcuts import redirect
def process_request(request):
    '''
    get the password from the get request
    compare the password to the expected value
    if it is same, redirect to login page
    '''
    if request.method == 'GET':
        password = request.GET.get('password')
        if password == 'admin':
            return redirect('/admin/')
        else:
            return HttpResponse('invalid password')
    else:
        return HttpResponse('invalid request')