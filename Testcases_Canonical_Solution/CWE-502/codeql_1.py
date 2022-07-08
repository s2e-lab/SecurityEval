from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    return un-pickled data
    '''
    return pickle.loads(pickled)