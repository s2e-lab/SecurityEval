import time
import threading
class CWE_488:
    def __init__(self):
        self.dataStart = 0
        self.dataLimit = 100
        self.thread = threading.currentThread()
    def getData(self):
        '''
        check if the dataStart is less than or equal to dataLimit
        if so, increase the dataStart by 1 and print which thread is currently accessing the data
        '''
        if self.dataStart <= self.dataLimit:
            self.dataStart+=1

        print("data from A :: "+str(self.dataStart)+" Accessor thread :: "+self.thread.threadId)
        time.sleep(0.5)