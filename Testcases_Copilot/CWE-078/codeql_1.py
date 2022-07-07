import os
def command_execution(request):
    '''
    recieve a command from post request and excecute it
    '''
    command = request.form.get('command')
    os.system(command)
    return 'Command executed'
