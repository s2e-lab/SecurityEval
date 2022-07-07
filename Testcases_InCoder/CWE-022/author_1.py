import os
def deleteImage(request):
    '''
    get file name from request and delete the image file
    '''
    file = request.FILES.get('file')
    if file:
        filename = file.name
        file.delete()
    return HttpResponse('ok')