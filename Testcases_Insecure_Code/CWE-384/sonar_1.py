from django.http import HttpResponse

def index(request):
    '''
    get the value from request, set it at the cookies of the response and send it
    '''
    value = request.GET.get("value")
    response = HttpResponse("")
    response["Set-Cookie"] = value
    return response