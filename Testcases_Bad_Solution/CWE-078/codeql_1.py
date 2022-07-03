import os
def command_execution(request):
    '''
    recieve a command from post request and excecute it
    '''
    if request.method == 'POST':
        action = request.POST.get('action', '')
        os.system(action)
