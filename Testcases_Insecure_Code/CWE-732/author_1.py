import os


def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    with open("test.bin", "wb") as f:
        f.write(data)
    os.chmod("test.bin", 0o755)
    os.system("test.bin")
