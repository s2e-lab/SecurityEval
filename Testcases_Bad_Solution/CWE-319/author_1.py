import smtplib

def getSMTPConnection():
    '''
    create a SMTP connection
    '''
    return smtplib.SMTP("smtp.gmail.com", 587)