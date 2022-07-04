
from django.http import HttpResponse

def process_request(request):
    '''
    get username and password from the request, check it for admin or normal user, and return appropriate response
    '''
