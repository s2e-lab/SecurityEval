from Crypto.PublicKey import DSA

def getPublicKey():
    '''
    return a DSA public key
    '''
    key = DSA.generate(2048)
    return key.publickey().exportKey('PEM')
