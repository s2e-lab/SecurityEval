from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''
    message = message.encode()
    ciphertext = DES_CIPHER.encrypt(message)
    channel.send(ciphertext)