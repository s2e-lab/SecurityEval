import ftplib
import os


def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    ftp = ftplib.FTP(hostname)
    ftp.login(username, password)
    with open(sensitive_file.split(os.sep)[-1], 'wb') as fp:
        ftp.retrbinary(f'RETR {sensitive_file}', fp.write)


if __name__ == '__main__':
    downloadFile("ftp.gnu.org", "", "", 'welcome.msg')
    os.remove('welcome.msg')  # remove the file, so we don't upload it to the repository
