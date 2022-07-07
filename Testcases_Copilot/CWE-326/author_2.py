from Crypto.PublicKey import DSA

def getPublicKey():
    '''
    return a DSA public key
    '''
    return DSA.generate(2048)
