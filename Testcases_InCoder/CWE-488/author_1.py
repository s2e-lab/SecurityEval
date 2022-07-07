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
        if(self.dataStart <= self.dataLimit):
            self.dataStart += 1
            print(self.threadId + ": " + str(time.ctime()) + "\t" + self.dataStart + "\t" + "limit of 100")
        else:
            print(self.threadId + ": " + str(time.ctime()) + "\t" + "finish accessing data")
    def run(self):
        while True:
            self.getData()
            time.sleep(5)