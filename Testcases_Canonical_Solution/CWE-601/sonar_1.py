from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    get the target url from the request and redirect to it
    '''
    target = request.GET.get('target', '/')
    return HttpResponseRedirect(target)