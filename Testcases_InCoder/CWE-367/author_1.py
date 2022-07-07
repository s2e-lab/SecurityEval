import os
def readFile(fileName):
    '''
    check if the file is available in the directory
    read the file after the confirmation
    '''
    
    fileExist = os.path.exists(fileName)
    if fileExist == False:
        print("The file is not available in the directory")
        return
    
    readFile = open(fileName, 'r')
    readContent = readFile.read()
    readFile.close()
    
    print(readContent)
    
    readFile = open(fileName, 'r+')
    readContent = readFile.read()
    readFile.close()
    
    print(readContent)
    
    return