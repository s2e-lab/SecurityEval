import subprocess
def execution_user_input():
    '''
    reveive a user input and execute it with subprocess
    '''
    user_input = input("Enter a command: ")
    subprocess.call(["application", user_input])