import tarfile

def extract_tar(file_name):
    '''
    open a file with tarfile and traverse each entry and extract in /tmp/ directory
    '''
    with tarfile.open('archive.zip') as tar:
        for entry in tar:
            tar.extract(entry, "/tmp/")

