
from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    filename = request.args['filename'][0].encode('utf-8')
    try:
        file = open(filename, 'rb')
    except IOError:
        return HTTPResponse(status=404)
    else:
        return HTTPResponse(body=file, content_type='application/octet-stream')
