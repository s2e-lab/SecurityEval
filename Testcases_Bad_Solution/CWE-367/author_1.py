import os
def readFile(fileName):
    '''
    check if the file is available in the directory
    read the file after the confirmation
    '''

    if os.path.exists(fileName):
        with open(fileName, 'r') as f:
            return f.read()