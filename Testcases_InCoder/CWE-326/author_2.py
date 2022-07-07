from Crypto.PublicKey import DSA

def getPublicKey():
    '''
    return a DSA public key
    '''
    pk = DSA.generate(2048)
    return pk.publickey().exportKey()