import base64

def code_execution(request):
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        exec("setname('%s')" % first_name)

