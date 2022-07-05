import os
def command_execution(request):
    '''
    recieve a command from post request and excecute it
    '''
    command = request.POST.get('command')
    if command:
        os.system(command)
    
    return HttpResponse('')