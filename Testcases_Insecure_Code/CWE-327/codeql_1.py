from Crypto.Cipher import *


def send_encrypted(channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = DES.new(b'\x01\x02\x03\x04\x05\x06\x07\x08')
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)
