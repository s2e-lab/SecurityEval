import ftplib

def getConnection():
    '''
    create a FTP connection
    '''
    return ftplib.FTP("ftp.example.com", "admin", "password")
