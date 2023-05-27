from django.http import HttpResponse


def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    '''