from django.http import HttpResponseRedirect, HttpResponse


def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    url = request.GET.get("next", "/")
    response = HttpResponse(status=302)
    response['Location'] = url
    return response
