import ftplib

def getConnection():
    '''
    create a FTP connection and return it
    '''
    ftp = ftplib.FTP('ftp.gmail.com')
    ftp.login('user', 'password')
    return ftp
