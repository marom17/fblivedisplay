"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: control_studioStatus.py
__Description__: Check if the studio is online

"""

import ssl
import config
import httplib
import json
from threading import Thread
import time

class OnlineStatus(Thread):
           
    def __init__(self,controller):
        Thread.__init__(self)
        self.running = True
        self.controller = controller
        
    def run(self):
        while self.running:
            self.controller.updateOnline(self.checkStatus())
            time.sleep(1)
            
    def checkStatus(self):
        host = config.commuthost
        port = config.commutport
        url = config.commuturl+config.commutchan
        c = httplib.HTTPSConnection(host,port,context=ssl._create_unverified_context(),timeout=1)
        try:
            c.request("GET", url)
            response = c.getresponse()
            data = response.read()
            data = json.loads(data)
            c.close()
            return data
        except:
            return False
    
    def stop(self):
        self.running = False