
from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    file_name = request.args.get('file_name')
    with open(file_name, 'rb') as file:
        data = file.read()
    return HTTPResponse(data)
