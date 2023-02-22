import threading
import time


def getData(dataStart, dataLimit, thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1 by, and then unlock the thread.
    Print which thread is currently accessing the data
    '''
    lock = threading.Lock()

    if dataStart <= dataLimit:
        lock.acquire()
        dataStart += 1
        lock.release()

    print("data from A :: " + str(dataStart) + " Accessor thread :: " + threading.get_ident())
    time.sleep(0.5)
