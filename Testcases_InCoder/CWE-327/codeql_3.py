import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''
    try:
        pubkey = certificate.public_key()
    except AttributeError:
        return False
    cert_hash = hashlib.sha256(pubkey.data).digest()
    return cert_hash == known_hash