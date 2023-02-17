import django.http


def route(request):
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    content_type = request.GET.get("Content-Type")
    response = django.http.HttpResponse()
    response.__setitem__('Content-Type', content_type)
    return response
