from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''
    cipher = DES.new('12345678')
    encrypted_message = cipher.encrypt(message)
    channel.send(encrypted_message)
    return encrypted_message
