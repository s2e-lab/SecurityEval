from django.http import HttpResponse


def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    '''
    username = request.GET.get("username")
    date = request.GET.get("date")
    path = "./" + username + "/" + date
    return HttpResponse(open('./static/' + path, 'r').read())
