import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''
    return hashlib.md5(certificate).hexdigest() == known_hash