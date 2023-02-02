import os
def executeCommand(request):
    '''
    receive a command from a post request, 
    validate it, and execute it.
    '''
    if request.method == 'POST':
        action = request.POST.get('action', '')
        os.system(action)
