from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    return pickled data
    '''
    return pickle.loads(pickled)