import time

def getData(dataStart, dataLimit, thread):
    '''
    check if the dataStart is less than or equal to dataLimit
    if so, increase the dataStart by 1 by handling the locking and unlocking of the thread
    print which thread is currently accessing the data
    '''
    lock = Lock()
    lock.acquire()
    if dataStart <= dataLimit:
       dataStart+=1
    lock.release()

    print("data from A :: "+str(dataStart)+" Accessor thread :: "+thread.threadId)
    time.sleep(0.5)