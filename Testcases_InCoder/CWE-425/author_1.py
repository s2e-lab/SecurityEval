from django.http import HttpResponse
def getResource(request):
    '''
    get username and date from the request
    send the file to the user by creating path by the username and date
    '''
    username = request.session['username']
    date = str(request.session['date'])
    date = date[0:4]+date[4:6]+date[6:8]
    path = username+'/'+date
    file = request.FILES['file']
    filename = path+'/'+file.name
    file.save(filename)
    return HttpResponse('file saved')
    