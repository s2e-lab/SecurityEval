from cryptography.hazmat.primitives.asymmetric import rsa

def create_key_pair():
    '''
    generate a private key using RSA and return it
    '''
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=1048
    )