import base64
def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    first_name = request.form.get('first_name')
    exec('setname("{}")'.format(base64.b64decode(first_name)))
    return 'Name set'
