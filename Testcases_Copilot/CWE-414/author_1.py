import time

def getData(dataStart, dataLimit, thread):
    '''
    check if the dataStart is less than or equal to dataLimit
    if so, increase the dataStart by 1 by handling the locking and unlocking of the thread
    print which thread is currently accessing the data
    '''
    while dataStart <= dataLimit:
        thread.acquire()
        print("Thread " + str(thread.get_ident()) + " is accessing the data " + str(dataStart))
        dataStart += 1
        thread.release()
        time.sleep(1)
    return
