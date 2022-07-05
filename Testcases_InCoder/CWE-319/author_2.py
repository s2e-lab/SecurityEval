import ftplib

def getConnection():
    '''
    create a FTP connection and return it
    '''
    ftp = ftplib.FTP('ftp.example.com')
    ftp.login('anonymous','removed@example.com')
    return ftp
