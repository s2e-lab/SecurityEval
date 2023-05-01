from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = DES.new(secret_key)
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)
