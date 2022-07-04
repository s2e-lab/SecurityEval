
from django.http import HttpResponse

def process_request(request):
    '''
    get username and password from the request, check it for admin or normal user, and return appropriate response
    '''
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username == 'admin' and password == 'admin':
        return HttpResponse('Admin')
    else:
        return HttpResponse('User')
