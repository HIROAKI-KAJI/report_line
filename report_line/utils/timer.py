""" timer class
timer class have now ,start time ,breaktime, end time and sum of worktime.
"""

import os
import time


class timer:
    STATE  = ["count","stop"]
    def __init__(self):
        self.tmp = time.time()
        self.count = time.time() - time.time()
        self.timelis = list()
        self.state = self.STATE[1]
        
        
    def start(self):
        self.tmp = time.time()
        self.state = self.STATE[0]
    def stop(self):
        self.stre_data()
        self.state = self.STATE[1]
    def end(self):
        self.stre_data()
        self.state = self.STATE[1]
    def stre_data(self):
        if self.state == timer.STATE[0]:
            now  = time.time()
            self.timelis.append([self.tmp,now])
            self.count += now - self.tmp
        
    def getdata(self):
        
        count = self.count
        if self.state == self.STATE[0]:
            now = time.time()
            count += now - self.tmp
        print(self.timelis)   
        return count
    
    
    
    
