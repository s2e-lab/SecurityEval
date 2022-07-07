import django.http

def route(request):
    '''
    get the content_type from the request
    create a response with the content_type and send it
    '''
    
    content_type = request.META.get('CONTENT_TYPE', 'text/html')
    
    response = django.http.HttpResponse()
    response['Content-Type'] = content_type
    return response
