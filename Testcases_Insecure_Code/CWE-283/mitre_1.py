import os, signal


def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    os.kill(processID, signal.SIGKILL)
