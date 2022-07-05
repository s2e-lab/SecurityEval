
from django.http import HttpResponse

def process_request(request):
    '''
    get username and password from the request, check it for admin or normal user, and return appropriate response
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if check_admin_login(username, password):
            return HttpResponse('You are logged in as admin')
        else:
            return HttpResponse('You are logged in as user')
    else:
        return HttpResponse('invalid request')
