import smtplib

def getSMTPConnection():
    '''
    create a SMTP connection and return it
    '''
    try:
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.ehlo()
        conn.login('removed@example.com','mypassword')
    except:
        traceback.print_exc()
        raise SMTPConnectionError
    return conn