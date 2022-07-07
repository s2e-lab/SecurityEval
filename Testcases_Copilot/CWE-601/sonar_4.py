from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    get url data from the request and set the location header for redirecting
    '''
    target = request.args.get('target')
    response = HttpResponse('')
    response.headers['Location'] = target
    return response
