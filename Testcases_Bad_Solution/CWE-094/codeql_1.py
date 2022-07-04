import base64
def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        exec("setname('%s')" % first_name)

