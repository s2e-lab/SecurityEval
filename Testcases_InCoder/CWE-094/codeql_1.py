import base64
def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    decoded_name = base64.decodestring(request.POST['first_name'])
    exec(decoded_name +'= exec("' + request.POST['first_name'] + '")')
    return render(request, 'code_execution.html')


