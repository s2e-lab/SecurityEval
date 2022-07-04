import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    with open("test.bin", "wb") as f:
        f.write(data)
    os.chmod("test.bin", 0o755)
    os.system("test.bin")