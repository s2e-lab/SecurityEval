from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    return un-pickled data
    '''
    data = pickle.load(open(pickled, 'rb'))
    return data
