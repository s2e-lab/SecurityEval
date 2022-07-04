from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''
    cipher = DES.new(b'\x01\x02\x03\x04\x05\x06\x07\x08')
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)