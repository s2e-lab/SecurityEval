import tarfile

def extract_tar(file_name):
    '''
    open a file with tarfile and traverse each entry and extract in /tmp/ directory
    '''
    tar = tarfile.open(file_name,"r:gz")
    tar.extractall(path='/tmp/')
    tar.close()
