import os
def deleteImage(request):
    '''
    get file name from request and delete the image file
    '''
    fileName = request.args.get('fileName')
    os.remove(fileName)
