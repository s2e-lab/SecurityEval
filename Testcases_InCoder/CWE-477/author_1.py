import time
  
def currentTime():
    '''
    print the current processor time in seconds
    '''
    
    start = time.time()
    
    end = time.time()
    
    print('Current time: %f sec' % (end-start))
    
    return end-start
    