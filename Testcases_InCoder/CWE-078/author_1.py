import subprocess
def execution_user_input():
    '''
    reveive a user input and execute it with subprocess
    '''
    cmd=input('enter a command: ')
    cmd=cmd.split(' ')
    cmd=subprocess.call(cmd)