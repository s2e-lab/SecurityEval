import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    hash = hashlib.md5(certificate).hexdigest()
    return hash == known_hash
