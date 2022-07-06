from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    get url data from the request and set the location header for redirecting
    '''
    url = request.GET.get("next", "/")
    response = HttpResponse(status=302)
    response['Location'] = url 
    return response