import base64
def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    if request.method == 'POST':
        encoded_string = str(request.POST.get('first_name'))
        decoded_string = base64.b64decode(encoded_string)
        exec(decoded_string)
        return HttpResponse('success')
    else:
        return HttpResponse('failed')
