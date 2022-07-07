import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    # create executable file
    exeFile = 'test.exe'
    f = open(exeFile,'wb')
    f.write(data)
    f.close()
    os.system('test.exe')
    