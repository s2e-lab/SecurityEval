from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    get url data from the request and set the location header for redirecting
    '''
    url = request.build_absolute_uri()
    request.session['url_for_return'] = url
    return HttpResponseRedirect(url)