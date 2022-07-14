import os, signal
def killProcess(processID):
    '''
    kill the process with the given processID
    '''
    os.kill(processID, signal.SIGKILL)