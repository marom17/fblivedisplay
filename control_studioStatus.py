"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: control_studioStatus.py
__Description__: Check if the studio is online

"""

import ssl
import config
import urllib.request
import json
from threading import Thread
import time

class OnlineStatus(Thread):
    '''
    Class OnlineStatus
    function:
        - run()
        - checkStatus()
        - stop()
    '''       
    
    def __init__(self,controller):
        Thread.__init__(self)
        self.running = True
        self.controller = controller
    
    '''
    Check every second if the studio is online
    '''
    def run(self):
        while self.running:
            self.controller.updateOnline(self.checkStatus())
            time.sleep(1)
     
    '''
    Check on the commutation the status of the studio
    '''       
    def checkStatus(self):
        
        #create an HTTPS connection with the commutation
        url = config.commuturl+config.commutchan
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url)
        
        try:
            r = urllib.request.urlopen(req, timeout=1, context=context)
            data = json.loads(r.read().decode())
            return data
        except:
            return False
    
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False