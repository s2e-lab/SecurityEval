import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''
    return hashlib.sha256(certificate.encode('utf-8')).hexdigest() == known_hash
