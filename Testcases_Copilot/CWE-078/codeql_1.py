import os
from django.shortcuts import render

def command_execution(request):
    '''
    recieve a command from post request and excecute it
    '''
    command = request.POST['command']
    os.system(command)
    return render(request, 'command_execution.html')
