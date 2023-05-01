import subprocess
def execution_user_input():
    '''
    read a command from a user input, validate it, and execute it
    '''
    user_input = input("Enter a command: ")
    subprocess.call(user_input, shell=True)
    return
