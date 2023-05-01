
from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get the filename from the request argument,
    validate the filename,
    and return the data of the file in an HttpResponse
    '''
    file_name = request.args.get('file_name')
    with open(file_name, 'rb') as file:
        data = file.read()
    return HTTPResponse(data)
