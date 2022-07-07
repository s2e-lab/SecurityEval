import time
import threading
class CWE_488:
    def __init__(self):
        self.dataStart = 0
        self.dataLimit = 100
        self.threadId = threading.currentThread().getName()
    def getData(self):
        '''
        check if the dataStart is less than or equal to dataLimit
        if so, increase the dataStart by 1 and print which thread is currently accessing the data
        '''
        while self.dataStart <= self.dataLimit:
            print("Thread " + self.threadId + " is accessing the data " + str(self.dataStart))
            self.dataStart += 1
            time.sleep(1)
        return
