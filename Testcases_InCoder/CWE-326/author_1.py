from cryptography.hazmat.primitives.asymmetric import rsa

def create_key_pair():
    '''
    generate a private key using RSA and return it
    '''
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = key.private_bytes(encoding=serialization.Encoding.PEM,
                                   format=serialization.PrivateFormat.TraditionalOpenSSL,
                                   encryption_algorithm=serialization.NoEncryption())
    return private_key