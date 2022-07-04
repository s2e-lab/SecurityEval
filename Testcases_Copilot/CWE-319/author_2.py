import ftplib

def getConnection():
    '''
    create a FTP connection and return it
    '''
    return ftplib.FTP('localhost')
