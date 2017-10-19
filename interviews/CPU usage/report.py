

import sys
import requests
import threading
import time
import HTML

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.number_of_request = 0
        self.number_of_response = 0
        self.noBreak = True
        self.total_elapsed_time = 0
        self.responseTime = 0

    def run(self):
        print "Starting " + self.name
        print "%s: %s" % (self.name, time.ctime(time.time()) )
        try:
            startedTime = time.time() #started
            while self.noBreak:
                self.number_of_request += 1
                response = requests.request('GET', 'http://localhost:8845')
                if response.status_code == 200:
                    self.responseTime = time.time() - startedTime
                    self.number_of_response += 1
                    print 'PASSED: %s test' % self.name
                else:
                    pass
                    print 'FAILED: %s Test. response value: %d' % (self.name ,response.status_code)
        except Exception as e:
            print e
        finally:
            self.total_elapsed_time = time.time() - startedTime
            print self.total_elapsed_time
            print "Exiting " + self.name

class Report(myThread):
    def __init__(self, threads):
        self.average_time_per_response = 0
        self.total_number_of_request = 0
        self.totalTime = 0
        self.threads = threads
        
    def startThreads(self):
        
        # Create 5 new threads
        thread1 = myThread(1, "Thread-1", 1)
        self.threads.append(thread1)     
        thread1.start()
        
        thread2 = myThread(2, "Thread-2", 1)
        self.threads.append(thread2)
        thread2.start()
        
        thread3 = myThread(3, "Thread-3", 1)
        self.threads.append(thread3)
        thread3.start()
        
        thread4 = myThread(4, "Thread-4", 1)
        self.threads.append(thread4)
        thread4.start()
        
        thread5 = myThread(1, "Thread-5", 1)
        self.threads.append(thread5)
        thread5.start()
        
        timeStarted = time.time()
        timeout = 5*60 #5 minutes
        while True:
            if time.time() - timeStarted >= timeout:
                break
        
        for t in self.threads:
            t.noBreak = False
            t.join()
         
        self.totalTime = time.time() - timeStarted    
def report():
    threads = []
    report = Report(threads)
    report.startThreads()
    print threads

    t = HTML.Table(header_row=['Thread Name', 'Request/s', 'Time/response', 'Request Total'])
    for thread in threads:
        t.rows.append([thread.name,thread.number_of_request / thread.total_elapsed_time,thread.responseTime / thread.number_of_response,thread.number_of_request])
    htmlcode = str(t)
    print htmlcode
    f = open('report.html','w')
    f.write(htmlcode)
    f.close()

if __name__ == '__main__':
    report()
