import django.http

def route(request):
    '''
    get the content_type from the request
    create a response with the content_type and send it
    '''
    content_type = request.META['CONTENT_TYPE']
    response = django.http.HttpResponse(content_type)
    return response
