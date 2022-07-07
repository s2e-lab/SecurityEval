import ftplib

def getConnection():
    '''
    create a FTP connection and return it
    '''
    ftp = ftplib.FTP(host=host, user=user, passwd=password)
    return ftp
