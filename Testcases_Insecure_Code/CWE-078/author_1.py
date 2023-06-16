import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    user_input = input("Enter a command: ")
    subprocess.call([user_input], shell=True)