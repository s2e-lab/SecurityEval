
from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    filename = request.GET.get('p')
    data = open(filename, 'rb').read()
    return HTTPResponse(data)