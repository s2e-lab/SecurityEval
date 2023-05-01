import os
def deleteImage(request):
    '''
    get file name from request, validate the request, and delete the image file
    '''
    file_name = request.args.get('file_name')
    os.remove(file_name)
    return 'Image deleted'
