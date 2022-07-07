from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''
    cipher = DES.new(password)
    cipher_text = cipher.encrypt(message)
    channel.send(cipher_text)