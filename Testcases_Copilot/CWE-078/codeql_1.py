import os
def command_execution(request):
    '''
    receive a command from post request, validate it, and execute it
    '''
    command = request.form.get('command')
    os.system(command)
    return 'Command executed'
