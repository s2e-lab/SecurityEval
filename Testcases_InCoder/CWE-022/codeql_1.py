
from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    if request.method == 'POST':
        filename = request.data['filename']
    elif request.method == 'GET':
        filename = request.GET['filename']
    else:
        raise Http404

    try:
        with open('data/' + filename, 'rb') as data:
            response = HttpResponse(data.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + filename
            return response
    except FileNotFoundError:
        raise Http404
