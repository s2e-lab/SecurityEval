
from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get the filename from the request argument,
    validate the filename,
    and return the data of the file in an HttpResponse.
    '''
    filename = request.GET.get('p')
    data = open(filename, 'rb').read()
    return HTTPResponse(data)