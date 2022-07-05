from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    return un-pickled data
    '''
    pkl_file = open('/home/amit/Desktop/pkl/'+pickled+'.pkl', 'rb')
    data = pickle.load(pkl_file)
    return data
