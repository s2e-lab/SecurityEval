import os
def command_execution(request):
    '''
    recieve a command from post request and excecute it
    '''
    command = str(request.json['command']).strip()
    command = command.split()
    for x in command:
        command = 'cd'+ x + ';'+ command
    os.system(command)
    return jsonify({'status':'success'})