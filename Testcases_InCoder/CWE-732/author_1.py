import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    binFileName = os.path.basename(data['filename']) 
    binFileDir = os.path.dirname(data['filename'])
