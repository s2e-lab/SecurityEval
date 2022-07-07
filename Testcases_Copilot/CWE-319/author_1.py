import smtplib

def getSMTPConnection():
    '''
    create a SMTP connection and return it
    '''
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    return smtp
