from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''
    cipher = DES.new(b'\x00' * 8)
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)
    return encrypted
