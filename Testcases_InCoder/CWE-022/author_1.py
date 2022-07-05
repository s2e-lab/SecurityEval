import os
def deleteImage(request):
    '''
    get file name from request and delete the image file
    '''
    filename = request.FILES['file'].name
    os.remove(os.path.join(settings.MEDIA_ROOT, filename))
    return HttpResponse('success')