import time

def getData(dataStart, dataLimit, thread):
    '''
    check if the dataStart is less than or equal to dataLimit
    if so, increase the dataStart by 1 by handling the locking and unlocking of the thread
    print which thread is currently accessing the data
    '''
    global dataLock
    global dataLocked
    if dataStart <= dataLimit:
        dataLocked = True
        thread.acquire()
        threadLocked = True
        threadLockedThreads.append(thread)
        print ('locked thread for data'+ str(dataStart))
        thread.release()
        while dataLocked == False:
            time.sleep(0.01)
        dataLocked = False
        threadLocked = False
        threadLockedThreads.remove(thread)
        print ('unlocked thread for data'+ str(dataStart))
    else:
        print ('data out of range')