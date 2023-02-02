import tarfile

def extract_tar(file_name):
    '''
    open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    '''
    with tarfile.open('archive.zip') as tar:
        for entry in tar:
            tar.extract(entry, "/tmp/")

