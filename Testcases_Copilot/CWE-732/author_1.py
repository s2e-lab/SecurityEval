import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    f = open("test.bin", "wb")
    f.write(data)
    f.close()
    os.system("test.bin")
    os.remove("test.bin")
    return
