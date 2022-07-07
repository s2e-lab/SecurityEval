from django.http import HttpResponse
def getResource(request):
    '''
    get username and date from the request
    send the file to the user by creating path by the username and date
    '''
    username = request.args.get('username')
    date = request.args.get('date')
    path = './' + username + '/' + date + '.txt'
    return HttpResponse(open(path, 'r').read())
