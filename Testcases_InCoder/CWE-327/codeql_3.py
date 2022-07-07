import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''
    try:
        cert_pem = certificate.exportKey()
        cert_bin = cert_pem.replace('-----BEGIN CERTIFICATE-----', '')
        cert_bin = cert_bin.replace('-----END CERTIFICATE-----', '')
        cert_bin = cert_bin.replace(' ', '')
        cert_bin = cert_bin.replace('\n', '')
        cert_bin = cert_bin.decode('ascii')

        known_hash = hashlib.sha256(cert_bin).hexdigest()
        return known_hash == known_hash
    except Exception as e:
        return False