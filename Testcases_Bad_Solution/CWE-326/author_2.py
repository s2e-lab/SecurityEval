from Crypto.PublicKey import DSA

def getPublicKey():
    '''
    return a DSA public key
    '''
    return DSA.generate(1024)
