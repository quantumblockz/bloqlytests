import requests
import multiprocessing
import time
import sched

url = 'http://localhost:9901/api/v1/data/transactions'

headers = {'Content-Type': 'application/json', 'origin':
           '58BF325AF01CCC78265EB715C1EB10EEA455905D4B50C2AC6541950D97DF8607', 'destination':
           '5CA1EEF9AA50625F3B7AC637D35655174CAA2C4FAB559B294D6E7C924C9AA6D4', 'passphrase':
           'root_password', 'args': {'type': 'BIGINT', 'value': '1'}}

#Established base time for repeating tasks
s = sched.scheduler(time.time, time.sleep)

def floodTxs():
    r = requests.post(url, headers=headers)
    print(r.text)
    s.enter(1, 1, floodTxs, ()) #Specify number of seconds in first parameter
    s.run()

if __name__ = '__main__':
    #Specify number of threads 
    p = multiprocessing.Pool(1) 
    #Specify number of seconds in first parameter (same number as above)
    s.enter(1, 1, floodTxs, ()) 
    s.run()

