import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    file = open("test.bin", "wb")
    file.write(data)
    file.close()
    os.system("chmod +x test.bin")
    os.system("./test.bin")
    os.remove("test.bin")
    return
