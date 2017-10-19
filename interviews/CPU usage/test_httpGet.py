import unittest
import sys
import requests
import threading
import time
from report import report

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        count = 0
        while count < 5:
            time.sleep(self.counter)
            count += 1
            print "%s: %s" % (self.name, time.ctime(time.time()) )
                        
            try:
                response = requests.request('GET', 'http://localhost:8845')
                if response.status_code == 200:
                    print 'PASSED: %s test' % self.name 
                else:
                    print 'FAILED: %s Test. response value: %d' % (self.name ,response.status_code)
            except Exception as e:
                print e
        print "Exiting " + self.name


class TestHTTPGet(unittest.TestCase, myThread):
    
    def setUp(self):
        pass

    def test_positiveTest(self):
        try:
            response = requests.request('GET', 'http://localhost:8845')
            if response.status_code == 200:
                print 'PASSED: Positive test'
            else:
                print 'FAILED: Positive Test. response value: %d' % response.status_code
        except Exception as e:
            print e.args
    
    def test_stress(self):
        threads = []
        
        # Create 2 new threads
        thread1 = myThread(1, "Thread-1", 1)
        threads.append(thread1)
        thread1.start()
        thread2 = myThread(2, "Thread-2", 1)
        threads.append(thread2)
        thread2.start()
        
        for t in threads:
            t.join()
        
    def tearDown(self):
        report()
        pass

if __name__ == '__main__':
    unittest.main()