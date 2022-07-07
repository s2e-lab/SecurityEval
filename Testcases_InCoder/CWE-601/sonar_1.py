from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    get the target url from the request and redirect to it
    '''
    target_url = request.GET['target_url']
    return HttpResponseRedirect(target_url)
